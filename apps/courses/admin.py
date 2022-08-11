from django.contrib import admin

from .models import Course, Enroll
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=('name', 'creator','money' ,'created_at')
    
class EnrollAdmin(admin.ModelAdmin):
    list_display=('user', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Enroll, EnrollAdmin)