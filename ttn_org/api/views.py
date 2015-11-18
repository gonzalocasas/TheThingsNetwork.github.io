from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group

from .models import IFGateways, IFNodes
from .serializers import UserSerializer, InfluxSerializer, MongoSerializer


DOCS_URL = "http://thethingsnetwork.org/wiki/Software/Overview#api"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IndexView(APIView):
    permission_classes = []

    def get(self, request, **kwargs):
        base_url = request.build_absolute_uri()
        index = {
            'docs': DOCS_URL,
            'nodes': "{}nodes/".format(base_url),
            'gateways': "{}gateways/".format(base_url),
        }
        return Response(index)


class GatewayView(APIView):
    permission_classes = []

    def get(self, request, eui=None, *args, **kwargs):
        queryset = IFGateways()
        #serializer = InfluxSerializer()
        serializer = MongoSerializer()

        sort_key = '-time'
        #query_params = {'order_by': sort_key}
        query_params = {'order_by': {'time': -1}}
        for key in ['time_span', 'limit', 'offset']:
            if request.GET.get(key):
                query_params[key] = request.GET.get(key)
        if eui:
            # gateway list
            query_params['eui'] = eui
        else:
            # gateway statuses overview
            query_params['group_by'] = 'eui'
            query_params['group_by_fields'] = { # mongo specific
                'eui': {'$last': '$eui'},
                'last_seen': {'$last': '$time'},
                'latitude': {'$last': '$latitude'},
                'longitude': {'$last': '$longitude'},
                'altitude': {'$last': '$altitude'},
                'altitude': {'$last': '$altitude'},
                'status_packets_count': {'$sum': 1},
            }
            #query_params['limit'] = 1
        items = queryset.get(**query_params)
        items = serializer.remap(items, sort_key=sort_key)
        response = Response(items, status=status.HTTP_200_OK)
        return response


class NodeView(APIView):
    permission_classes = []

    def get(self, request, node_eui=None, *args, **kwargs):
        queryset = IFNodes()
        #serializer = InfluxSerializer()
        serializer = MongoSerializer()

        sort_key = '-time'
        #query_params = {'order_by': sort_key}
        query_params = {'order_by': {'time': -1}}
        for key in ['time_span', 'limit', 'offset']:
            if request.GET.get(key):
                query_params[key] = request.GET.get(key)
        if node_eui:
            # node packets list
            #query_params['group_by'] = 'gateway_eui'
            query_params['nodeeui'] = node_eui
        else:
            # node overview
            query_params['group_by'] = 'nodeeui'
            query_params['group_by_fields'] = { # mongo specific
                'node_eui': {'$last': '$nodeeui'},
                'last_seen': {'$last': '$time'},
                'last_gateway_eui': {'$last': '$gateway_eui'},
                'packets_count': {'$sum': 1},
            }
            #query_params['limit'] = 1
        items = queryset.get(**query_params)
        items = serializer.remap(items, sort_key=sort_key)
        items = serializer.annotate(items)
        response = Response(items, status=status.HTTP_200_OK)
        return response

