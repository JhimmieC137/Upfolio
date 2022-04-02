# from tkinter import Image
from email.mime import image
from tkinter import image_names
from django.shortcuts import render
from django.http import request
from .models import Info, Team

# Create your views here.
def home(request):
    return render(request, 'home.html')



def index(request):
    Information = Info.objects.all()
    team = Team.objects.all()
    # image = pics[(1)]
    # icon = image   
    return render(request, 'index.html', {'Information' : Information, 'team' : team})

def about_upfolio(request):
    return render(request, 'about_upfolio.html')

def volunteers(request):
    return render(request, 'volunteers.html')

def resource_pg(request):
    return render(request, 'resource_page.html')