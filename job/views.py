# from tkinter import Image
from email.mime import image
from tkinter import image_names
from django.shortcuts import render, redirect
from django.http import request
from .models import Info, Team
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')



def index(request):
    information = Info.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {'information' : information, 'team' : team})

def about_upfolio(request):
    Information = Info.objects.all()
    team = Team.objects.all()
    return render(request, 'about_upfolio.html', {'Information' : Information, 'team' : team})

def team(request):
    return render(request, 'team.html')

def volunteers(request):
    return render(request, 'volunteers.html')

def resource_pg(request):
    return render(request, 'resource_page.html')