from rest_framework import serializers
# from apps.accounts.models import User, UserManager
from django.contrib.auth.models import User
from ..courses.models import Course, Enroll, Video
from ..freelanceshala.models import Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = '__all__'

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enroll
        fields='__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'