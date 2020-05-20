from django.urls import path
from . import views


# Defines the url paths for all links in the 'projects' app
urlpatterns = [
    # path('', views.home, name='projects-home'),
    path('about_me/', views.about_me, name='about_me'),
    path('resume/', views.resume, name='resume'),
]