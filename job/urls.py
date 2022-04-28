from django.urls import path 
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about_upfolio/', views.about_upfolio, name='about_upfolio'),
    path('team/', views.team, name='team'),
    path('mailing_list_form/', views.mailing_list_form, name='mailing_list_form'),
    path('resource_page/', views.resource_pg, name='resource_page'),
    path('volunteers/', views.volunteers, name='volunteer_with_upfolio'),
]