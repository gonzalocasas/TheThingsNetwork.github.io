from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        item = {'foo': 'bar'}
        response = Response(item, status=status.HTTP_200_OK)
        return response
