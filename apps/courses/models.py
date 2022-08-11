from datetime import datetime, timezone

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from django.contrib.auth.models import User

# Create your models here.


class CourseManager(models.Manager):
    use_in_migrations=True
    def create_course(self, name, description,user_id, money):
        if name is None:
            raise TypeError('COurse should have a name')
        if description is None:
            raise TypeError('Course must have a description')
        if money is None:
            raise TypeError('Cost is not mentioned')
        course = self.model(name=name, description=description,creator=user_id, money=money)
        course.save(self.db)
        return course
    
class EnrollManager(models.Manager):
    use_in_migrations=True
    def create_enroll(self, user_id, course_id):
        enroll = self.model(user=user_id, course=course_id)
        enroll.save(self.db)
        return enroll
    
        

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(max_length=400, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.FloatField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.name
    
    objects=CourseManager()
    

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    objects=EnrollManager()
    