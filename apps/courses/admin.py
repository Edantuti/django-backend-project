from django.contrib import admin

from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class CourseAdmin(admin.ModelAdmin):
    list_display=('name', 'creator','money' ,'created_at')
    
class EnrollAdmin(admin.ModelAdmin):
    list_display=('user', 'course')
    
class VideoAdmin(admin.ModelAdmin):
    list_display=('name', 'course', 'video', 'created_at')
    
class LessonAdmin(admin.ModelAdmin):
    list_display=('info', 'course')
    
class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text', 'lesson')
    fieldsets=[
        ('Question', {'fields':['question_text', 'lesson']}),
    ]
    inlines=[ChoiceInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
