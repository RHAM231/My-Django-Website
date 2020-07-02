from django.shortcuts import render
from django.apps import apps
from . models import (Skill)


def home(request):
    Project = apps.get_model('projects', 'Project')
    context = {
        'iconskills': Skill.objects.all(),
        'projects': Project.objects.all().order_by('index_key')
    }
    return render(request, 'base_pages/home.html', context)


def about_me(request):
    return render(request, 'base_pages/about_me.html', {'title': 'About'})


def resume(request):
    return render(request, 'base_pages/resume.html', {'title': 'Resume'})
