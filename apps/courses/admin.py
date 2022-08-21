from django.contrib import admin

from .models import Course, Enroll, Video
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=('name', 'creator','money' ,'created_at')
    
class EnrollAdmin(admin.ModelAdmin):
    list_display=('user', 'course')
    
class VideoAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'video')

admin.site.register(Course, CourseAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Video, VideoAdmin)