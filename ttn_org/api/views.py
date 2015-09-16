from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group

from .models import IFGateways
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GatewayView(APIView):
    permission_classes = []

    def get(self, request, eui=None, *args, **kwargs):
        queryset = IFGateways()
        print("COMING IN", eui)
        if eui:
            items = queryset.get(time_span='4d', eui=eui)
        else:
            items = queryset.get(time_span='4d')
        response = Response(items, status=status.HTTP_200_OK)
        return response

