# from tkinter import Image
from email import message
from email.mime import image
from tkinter import image_names
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import request
from django.http import HttpResponseRedirect
from .models import Info, Team, Daily_Opportunie
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SubscriptionForm
# import requests
import time
from rest_framework import status
from rest_framework.response import Response
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

def job_vacancies(request):
    return render(request, 'job_vacancies.html')

def internships(request):
    return render(request, 'internships.html')

def grants(request):
    return render(request, 'grants.html')

def online_courses(request):
    return render(request, 'online_courses.html')

def scholarships(request):
    return render(request, 'scholarships.html')

def fellowships(request):
    return render(request, 'fellowships.html')

def competitions(request):
    return render(request, 'competitions.html')

def daily_opportunities(request):
    opportunities = Daily_Opportunie.objects.all()
    return render(request, 'daily_opportunities.html', {'opportunities': opportunities})

def mailing_list_form(request):
    submitted = False
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            url = 'https://bit.us4.list-manage.com/subscribe/post?u=6626aa149ad8c147094e0d282&amp;id=fbdc92be1f'
            payload = {'Token':'My-Secret_Token', 'EMAIL': request.POST.get("email"), 'FNAME':request.POST.get("first_name"), 'LNAME':request.POST.get("Last_name"), 'MMERGE6':request.POST.get("phone"), 'birthday':request.POST.get("birthday") }
            r = request.POST(url, data = payload)
            if r .status_code == 200:
                data =r.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return HttpResponseRedirect(reverse("mailing_list_form") + '?submitted=True')
        else:
            messages.info(request,'Please enter a valid Phone number')
            print("Something's wrong", form)
    else:
        form = SubscriptionForm
        if 'submitted' in request.GET:
            submitted=True
            print("I'm Here!!!")
            
    return render(request, 'mailing_list_form.html', {'form':form, 'submitted':submitted})