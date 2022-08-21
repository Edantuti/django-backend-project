from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
 
from django.utils.translation import gettext_lazy as _
 
 
 
class UserManager(BaseUserManager):
   use_in_migrations=True
   def _create_user(self, username, email, password, **args):
       user = self.model(username=username, email=email, **args)
       user.password=make_password(password)
       user.save(using=self.db)
      
   def create_user(self, username, email, password, **args):
       args.setdefault("is_staff", False)
       args.setdefault("is_superuser", False)
       return self._create_user(username, email, password, **args)
   def create_staffuser(self, username, email, password, **args):
       args.setdefault("is_staff", True)
       args.setdefault("is_superuser", False)
       return self._create_user(username, email, password, **args)
  
   def create_superuser(self, username, email, password, **args):
       args.setdefault("is_staff", True)
       args.setdefault("is_superuser", True)
       return self._create_user(username, email, password, **args)
 
 
class User(AbstractUser):
   is_freelancer=models.BooleanField(_("Freelancer status"), default=False)
   birth_date=models.DateField(_("birth date"), blank=True, null=True)
  
   objects = UserManager()
    
   REQUIRED_FIELDS = ['email']
 
   class Meta(AbstractUser.Meta):
       swappable = "AUTH_USER_MODEL"
       
      
      
    