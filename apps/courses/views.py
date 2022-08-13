from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FileUploadParser

# from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, CAP_PROP_FPS
from .forms import VideoForm
from . import video
from ..freelanceshala.models import Order
from .models import Course, Enroll, Video
from ..api.serializers import CourseSerializer, EnrollSerializer, VideoSerializer
# Create your views here.


class CourseData(APIView):
    def get(self, request, format=None):
        course = Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.POST
        Course.objects.create_course(name=data.get("name"), description=data.get("description"),user_id=request.user,money=data.get("money"))
        return Response(request.data)
        
    
class CourseDetail(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(name__iexact=pk)
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
            course=Course.objects.get(name__iexact=data.get("course_name"))
        except Course.DoesNotExist:
            return Http404
        enroll = Enroll.objects.create_enroll(request.user, course)
        Order.objects.create(enroll=enroll)
        return Response(request.data)
    
class VideoData(APIView):
    # parser_classes=(MultiPartParser)
    parser_classes=(MultiPartParser,FileUploadParser,)
    
    def get(self, request, format=None):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        
        return Response(request.data)
    
    def post(self, request, format=None):
        data=request.POST
        try:
            course = Course.objects.get(name__iexact=data.get("course")) 
        except Course.DoesNotExist:
            raise TypeError("Course doesn't exist")
        Video.objects.create_video_db(name=request.FILES["video"].name, video=request.FILES["video"], course=course)
        
        
        return Response(request.data["course"])
    
    
class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(course=pk)
        except Video.DoesNotExist:
            raise TypeError("Video Doesn't exist")
    def get(self, request, format=None):
        try:
            course=Course.objects.get(name_iexact=request.data.get("course"))
        except Course.DoesNotExist:
            raise TypeError("Course doesn't exist")
        video = self.get_object(course.id)
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)
        
        