from socket import fromshare
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from.models import Subscribe

#Create subscribers

class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"
        
        
        widgets = {
                'email':forms.EmailInput(attrs={'class':'input--style-4'}),
                'first_name':forms.TextInput(attrs={'class':'input--style-4'}),
                'last_name':forms.TextInput(attrs={'class':'input--style-4'}),
                'phone':forms.TextInput(attrs={'class':'input--style-4', 'type':'tel', 'id':'phone'}),
                'birthday':forms.TextInput(attrs={'class':'input--style-5', 'type':'date'}),
        }