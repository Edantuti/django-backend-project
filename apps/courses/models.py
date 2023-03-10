from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
from django.utils import timezone

class CourseManager(models.Manager):
    use_in_migrations=True
    def create_course(self, name, description,user, money):
        if name is None:
            raise TypeError('Course should have a name')
        if description is None:
            raise TypeError('Course must have a description')
        if money is None:
            raise TypeError('Cost is not mentioned')
        course = self.model(name=name, description=description,creator=user, money=money)
        course.save(self.db)
        return course
    
class EnrollManager(models.Manager):
    use_in_migrations=True
    def create_enroll(self, user, course):
        enroll = self.model(user=user, course=course)
        enroll.save(self.db)
        return enroll
    
class VideoManager(models.Manager):
    use_in_migrations=True
    
    def create_video_db(self,name ,video, course):
        video = self.model(name=name, course=course, video=video)
        video.save(self.db)
        return video
    
    def create_directory(instance, filename):
        return f'videos/{instance.course}/{filename}'

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(max_length=400, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.FloatField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return self.name
    
    objects=CourseManager()
    

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= "enroll"
        
    def __str__(self):
        return self.user.name + self.course.name
    
    objects=EnrollManager()
    

class Video(models.Model):
    name=models.CharField(max_length=200)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    video=models.FileField(upload_to=VideoManager.create_directory)
    created_at = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="video"
    
    objects=VideoManager()


class Lesson(models.Model):
    info=models.TextField(editable=True, max_length=300)
    course=models.ForeignKey(to=Course,on_delete=models.CASCADE)
    
    
    
class Question(models.Model):
    lesson=models.ForeignKey(to=Lesson,on_delete=models.CASCADE)
    question_text=models.CharField(max_length=200)
    
    
class Choice(models.Model):
    question=models.ForeignKey(to=Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)
    correct=models.BooleanField(default=False, editable=True)
    
    
    
