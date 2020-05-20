from django.shortcuts import render
from . models import (Project, IconSkill)

# Renders the home page.
# 'iconskills' pulls skills with their associated pictures from the database
# 'projects' renders projects from the database
# def home(request):
#     context = {
#         'iconskills': IconSkill.objects.all(),
#         'projects': Project.objects.all().order_by('index_key')
#     }
#     return render(request, 'projects/home.html', context)


# Renders the about me page
def about_me(request):
    return render(request, 'base_pages/about_me.html', {'title': 'About'})


# Renders the resume page
def resume(request):
    return render(request, 'base_pages/resume.html', {'title': 'Resume'})
