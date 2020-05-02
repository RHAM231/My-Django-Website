from django.urls import path
from . import views
# from . views import (
#     CheckListView
# )


urlpatterns = [
    path('', views.home, name='projects-home'),
    path('portfolio-project/', views.portfolio_project,
         name='projects-portfolio-project'),
    path('project2/', views.project2, name='projects-project2'),
    path('project3/', views.project3, name='projects-project3'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('resume/', views.resume, name='resume'),
    path('portfolio-project/project_checklist/', views.checklist,
         name='project_checklist'),
    # path('portfolio-project/project_checklist', CheckListView.as_view(),
    #      name='project_checklist'),
]
