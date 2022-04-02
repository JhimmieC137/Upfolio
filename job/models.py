from django.db import models

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
    