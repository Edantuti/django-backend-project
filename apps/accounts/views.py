import json
from django.shortcuts import render
from django.http import Http404

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from apps.api.serializers import UserSerializer

# Create your views here.

class UserData(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        data = request.POST
        User.objects.create_user(username=data.get("username", 0),password=data.get("password", 0))
        return Response("Done!\n")
    
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id__exact=pk)
        except User.DoesNotExist:
            return Http404
            
    def get(self, request,pk, format=None):
        serializer = UserSerializer(self.get_object(pk))
        return Response(serializer.data)