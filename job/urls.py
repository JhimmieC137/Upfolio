from django.urls import path 
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about_upfolio/', views.about_upfolio, name='about_upfolio'),
    path('team/', views.team, name='team'),
    path('job_vacancies/', views.job_vacancies, name='job_vacancies'),
    path('internships/', views.internships, name='internships'),
    path('grants/', views.grants, name='grants'),
    path('online_courses/', views.online_courses, name='online_courses'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('fellowships/', views.fellowships, name='fellowships'),
    path('competitions/', views.competitions, name='competitions'),
    path('daily_opportunities/', views.daily_opportunities, name='daily_opportunities'),
    path("mailing_list_form/", views.mailing_list_form, name='mailing_list_form'),
]