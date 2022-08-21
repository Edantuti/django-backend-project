from django.contrib import admin
# from .models import User
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

class UsersAdmin(admin.ModelAdmin):
    list_display=('email', 'is_staff', 'is_active', 'is_freelancer')


admin.site.register(User, UsersAdmin)