from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group

from .models import IFGateways, IFNodes
from .serializers import UserSerializer, InfluxSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GatewayView(APIView):
    permission_classes = []

    def get(self, request, eui=None, *args, **kwargs):
        queryset = IFGateways()
        serializer = InfluxSerializer()
        if eui:
            items = queryset.get(time_span='4d', eui=eui)
        else:
            items = queryset.get(time_span='4d', group_by='eui', limit=1)
        items = serializer.remap(items)
        response = Response(items, status=status.HTTP_200_OK)
        return response


class NodeView(APIView):
    permission_classes = []

    def get(self, request, node_eui=None, *args, **kwargs):
        queryset = IFNodes()
        serializer = InfluxSerializer()
        if node_eui:
            items = queryset.get(time_span='4d', node_eui=node_eui)
        else:
            items = queryset.get(time_span='4d', group_by='node_eui', limit=1)
        items = serializer.remap(items)
        items = serializer.annotate(items)
        response = Response(items, status=status.HTTP_200_OK)
        return response

