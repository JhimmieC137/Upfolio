from datetime import date, datetime
from tkinter import image_names
from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth.models import User, auth
from django.contrib import messages
from psycopg2 import Date
import phonenumbers
# Create your views here.


# def register(request):
def mailing_list_form(request):
    if request.method == 'POST':
        username=request.POST['first_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        
        caller_address=phonenumbers.parse(phone)
        if phonenumbers.is_valid_number(caller_address) == False:
            messages.info(request, 'Please use a correct phone number')
            return redirect('mailing_list_form')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already registered')
            return redirect('mailing_list_form')
        else:
            # user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, gender=gender, phone=phone, address=address)
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, gender=gender, email=email, phone=phone, address=address)
            User.__init__(self=user, **extra_fields)
            user.save();
            messages.info(request, 'Registration successful')
    
    else:
        return render(request, 'mailing_list_form.html')
