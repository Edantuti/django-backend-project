from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..freelanceshala.models import Order


from .models import Course, Enroll
from apps.api.serializers import CourseSerializer, EnrollSerializer
# Create your views here.


class CourseData(APIView):
    def get(self, request, format=None):
        course = Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.POST
        if data.get("username") != None:
            try:
                user = User.objects.get(username__icontains=data.get("username"))
            except User.DoesNotExist:
                return Http404
        else:
            raise TypeError('Username must be included')
        Course.objects.create_course(name=data.get("name", 0), description=data.get("description"),user_id=user,money=data.get("money"))
        return Response(request.data)
        
    
class CourseDetail(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(name__icontains=pk)
        except Course.DoesNotExist:
            return Http404
        
    def get(self,request, pk, format=None):
        serializer = CourseSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        serializer = CourseSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class EnrollData(APIView):
    def get(self, request, format=None):
        enroll=Enroll.objects.all()
        serializer=EnrollSerializer(enroll, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data=request.POST
        try:
            user=User.objects.get(username__icontains=data.get("username"))
        except User.DoesNotExist:
            return Http404
        try:
            course=Course.objects.get(name__exact=data.get("course_name"))
        except Course.DoesNotExist:
            return Http404
        enroll = Enroll.objects.create_enroll(user, course)
        print(enroll)
        Order.objects.create(enroll=enroll)
        return Response(request.data)
        