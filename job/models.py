from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class Info(models.Model):
    heading = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    about = models.CharField(max_length=100, null=True)
    

class Images(models.Model):
    img = models.ImageField(upload_to= 'media')
    description = models.CharField(max_length=200, null=True) 

class Team(models.Model):
    job_title = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, null=True)
    name = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to= 'media')
    
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_of_birth = models.IntegerField(verbose_name='date_of_birth')
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)