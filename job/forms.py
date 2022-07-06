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
                'email':forms.EmailInput(attrs={'class':'input--style-4', 'type':'email', 'name':'EMAIL', 'id':'mce-EMAIL', 'value':''}),
                'first_name':forms.TextInput(attrs={'class':'input--style-4', 'type':'text', 'name':'FNAME', 'id':'mce-FNAME', 'value':''}),
                'last_name':forms.TextInput(attrs={'class':'input--style-4', 'type':'text', 'name':'LNAME', 'id':'mce-LNAME', 'value':''}),
                'phone':forms.TextInput(attrs={'class':'input--style-4', 'type':'tel', 'name':'MMERGE6', 'id':'phone', 'value':''}),
                # 'birthday':forms.TextInput(attrs={'class':'input--style-5' 'birthday', 'type':'date', 'name':'MMERGE7[month]', 'id':'mce-MMERGE7-day' 'mce-MMERGE7-day',}),
        }