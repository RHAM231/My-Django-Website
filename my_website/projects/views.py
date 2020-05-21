from django.shortcuts import render
from django.apps import apps
from . models import (
    Project,
    CheckListHeader,
    LinkHeader,
    ProjectSummary,
    ProjectSummaryList,
    ProjectDescription,
    ProjectDescriptionList,
)


# Renders web pages specific to the 'projects' app.


# Renders the home page.
# 'iconskills' pulls skills with their associated pictures from the database
# 'projects' renders projects from the database
def home(request):
    # Let's load the 'Skill' model from the base_pages app and pass it into context
    Skill = apps.get_model('base_pages', 'Skill')
    context = {
        'iconskills': Skill.objects.all(),
        'projects': Project.objects.all().order_by('index_key')
    }
    return render(request, 'projects/home.html', context)


# Renders the project description page for the django website.
# The lists and bodies of texts are all stored in the database.
def portfolio_project(request):
    context = {
        'projectsummaries': ProjectSummary.objects.all().order_by('index_key'),
        'projectsumlists': ProjectSummaryList.objects.all().order_by('index_key'),
        'projectdescriptions': ProjectDescription.objects.all().order_by('index_key'),
        'projectdeslists': ProjectDescriptionList.objects.all().order_by('index_key'),
        'title': 'Projects'
    }
    return render(request, 'projects/portfolio_project.html', context)


# Renders the project description page for project 2
def project2(request):
    return render(request, 'projects/project2.html', {'title': 'Projects'})


# Renders the project description page for project 3
def project3(request):
    return render(request, 'projects/project3.html', {'title': 'Projects'})


# Renders the about me page
# def about_me(request):
#     return render(request, 'projects/about_me.html', {'title': 'About'})


# Renders the resume page
# def resume(request):
#     return render(request, 'projects/resume.html', {'title': 'Resume'})


# Renders the checklist page. Entries and headers are stored in the database
def checklist(request):
    context = {
        'headers': CheckListHeader.objects.all().order_by('indexkey'),
        'linkheaders': LinkHeader.objects.all(),
        'title': 'Checklist'
    }
    return render(request, 'projects/project_checklist.html', context)
