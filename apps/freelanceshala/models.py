from datetime import datetime
from django.db import models

from apps.courses.models import Enroll
# Create your models here.

class Order(models.Model):
    enroll=models.ForeignKey(Enroll, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    
    

# class FreelanceOrder(Order):
#     pass
    