from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import get_user_model
 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
 
from ..api.serializers import UserSerializer
 
# Create your views here.

User=get_user_model()
 
class UserData(APIView):
   def get(self, request, format=None):
       # permission_classes=['permission.isAuthenticated, TokenHasScope']
       user = User.objects.all()
       serializer = UserSerializer(user, many=True)
       return Response(serializer.data)
   def post(self, request, format=None):
       #permission_classes=['permission.isAuthenticated, TokenHasReadWriteScope']
       data = request.POST
       staff = data.get("is_staff")
       superuser = data.get("is_superuser")
       if not staff and not superuser:
           User.objects.create_user(username=data.get("username", 0),email=data.get("email", 0),password=data.get("password", 0))
       if staff and not superuser:
           User.objects.create_staffuser(username=data.get("username", 0),email=data.get("email", 0),password=data.get("password", 0))
       if superuser:
           User.objects.create_superuser(username=data.get("username", 0),email=data.get("email", 0),password=data.get("password", 0))
       return Response("Done!\n")
  
class UserDetail(APIView):
   def get_object(self, pk):
       try:
           return User.objects.get(id__exact=pk)
       except User.DoesNotExist:
           return Http404
          
   def get(self, request,pk, format=None):
       # permission_classes=['permission.isAuthenticated, TokenHasScope']
       serializer = UserSerializer(self.get_object(pk))
       return Response(serializer.data)