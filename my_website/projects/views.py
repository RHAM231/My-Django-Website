from django.shortcuts import render
from . models import (
    CheckListHeader,
    LinkHeader,
    ProjectSummary,
    ProjectSummaryList,
    ProjectDescription,
    ProjectDescriptionList,
)


def portfolio_project(request):
    context = {
        'projectsummaries': ProjectSummary.objects.all().order_by('index_key'),
        'projectsumlists': ProjectSummaryList.objects.all().order_by('index_key'),
        'projectdescriptions': ProjectDescription.objects.all().order_by('index_key'),
        'projectdeslists': ProjectDescriptionList.objects.all().order_by('index_key'),
        'title': 'Projects'
    }
    return render(request, 'projects/portfolio_project.html', context)


def project2(request):
    return render(request, 'projects/project2.html', {'title': 'Projects'})


def project3(request):
    return render(request, 'projects/project3.html', {'title': 'Projects'})


def checklist(request):
    context = {
        'headers': CheckListHeader.objects.all().order_by('indexkey'),
        'linkheaders': LinkHeader.objects.all(),
        'title': 'Checklist'
    }
    return render(request, 'projects/project_checklist.html', context)
