from rest_framework import serializers
# from apps.accounts.models import User, UserManager
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        