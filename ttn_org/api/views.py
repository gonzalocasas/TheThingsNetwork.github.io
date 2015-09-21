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


class IndexView(APIView):
    permission_classes = []

    def get(self, request, **kwargs):
        base_url = request.build_absolute_uri()
        index = {
            'nodes': "{}nodes/".format(base_url),
            'gateways': "{}gateways/".format(base_url),
        }
        return Response(index)


class GatewayView(APIView):
    permission_classes = []

    def get(self, request, eui=None, *args, **kwargs):
        queryset = IFGateways()
        serializer = InfluxSerializer()

        query_params = {'order_by': '-time'}
        for key in ['time_span', 'limit', 'offset']:
            if request.GET.get(key):
                query_params[key] = request.GET.get(key)
        if eui:
            # gateway list
            query_params['eui'] = eui
        else:
            # gateway statuses overview
            query_params['group_by'] = 'eui'
            query_params['limit'] = 1
        items = queryset.get(**query_params)
        items = serializer.remap(items)
        response = Response(items, status=status.HTTP_200_OK)
        return response


class NodeView(APIView):
    permission_classes = []

    def get(self, request, node_eui=None, *args, **kwargs):
        queryset = IFNodes()
        serializer = InfluxSerializer()

        query_params = {'order_by': '-time'}
        for key in ['time_span', 'limit', 'offset']:
            if request.GET.get(key):
                query_params[key] = request.GET.get(key)
        if node_eui:
            # node packets list
            query_params['node_eui'] = node_eui
        else:
            # node overview
            query_params['group_by'] = 'node_eui'
            query_params['limit'] = 1
        items = queryset.get(**query_params)
        items = serializer.remap(items)
        items = serializer.annotate(items)
        response = Response(items, status=status.HTTP_200_OK)
        return response

