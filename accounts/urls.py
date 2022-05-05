from django.urls import path 
from .import views


urlpatterns = [
    path("mailing_list_form/", views.mailing_list_form, name="mailing_list_form")
]
