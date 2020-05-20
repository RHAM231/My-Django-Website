from django.urls import path
from . import views
from contact import views as contact_views


# Defines the url paths for all links in the 'projects' app
urlpatterns = [
    path('', views.home, name='projects-home'),
    path('portfolio-project/', views.portfolio_project, name='projects-portfolio-project'),
    path('project2/', views.project2, name='projects-project2'),
    path('project3/', views.project3, name='projects-project3'),
    # path('about_me/', views.about_me, name='about_me'),
    path('contact-me/', contact_views.contact_me, name='contact_me'),
    # path('resume/', views.resume, name='resume'),
    path('portfolio-project/project_checklist/', views.checklist, name='project_checklist'),
]
