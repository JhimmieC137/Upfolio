from optparse import Option
from xml.dom.xmlbuilder import Options
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser
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
    
class Subscribe(models.Model):
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField()
    birthday = models.CharField(max_length=15, null=True)


class Daily_Opportunie(models.Model):
    name = models.CharField(max_length=20, null=False)
    pic = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    