from django.db import models
from django.contrib.auth.models import *
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, fullname, phone_No, password=None, password2=None):
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          fullname=fullname,
          phone_No= phone_No
      )

      user.set_password(password)
      user.is_editor = True
      user.is_staff= True
      user.save(using=self._db)
      return user

  def create_superuser(self, email, fullname, phone_No, password=None):
      user = self.create_user(
          email,
          password=password,
          fullname=fullname,
          phone_No= phone_No
      )
      user.is_staff= True
      user.is_superuser =True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  fullname = models.CharField(max_length=200)
  is_editor = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff= models.BooleanField(default=True)
  phone_No = models.CharField(max_length=150, null=True, blank=True)
  image = models.ImageField(upload_to="image/", null=True, blank=True)
  address = models.CharField(max_length=150, null=True, blank=True)
  created_at = models.DateField(auto_now_add=True, null=True, blank=True)
  updated_at = models.DateField(auto_now=True, null=True, blank=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['fullname','phone_No']

  def __str__(self):
      return self.fullname

  
 

    
  





