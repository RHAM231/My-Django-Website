from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='projects-home'),
    path('about_me/', views.about_me, name='about_me'),
    path('resume/', views.resume, name='resume'),
]