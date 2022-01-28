from django.shortcuts import render
from django.apps import apps
from . models import (Skill)


'''
Renders the home page. 'iconskills' pulls skills with their 
associated pictures from the database. 'projects' renders projects
from the database
'''
def home(request):
    # Let's load the 'Project' model from the base_pages app and pass
    # it into context
    Project = apps.get_model('projects', 'Project')
    context = {
        'iconskills': Skill.objects.all(),
        'projects': Project.objects.all().order_by('index_key')
    }
    return render(request, 'base_pages/home.html', context)


# Renders the about me page
def about_me(request):
    return render(request, 'base_pages/about_me.html', {'title': 'About'})


# Renders the resume page
def resume(request):
    return render(request, 'base_pages/resume.html', {'title': 'Resume'})
