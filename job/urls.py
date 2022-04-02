from django.urls import path 
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('about_upfolio/', views.about_upfolio, name='about_upfolio'),
    path('resource_page/', views.resource_pg, name='resource_page'),
    path('volunteers/', views.volunteers, name='volunteer_with_upfolio'),
]