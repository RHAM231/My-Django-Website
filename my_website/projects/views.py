from django.shortcuts import render
from . models import (
    Project,
    CheckListHeader,
    LinkHeader,
    ProjectSummary,
    ProjectSummaryList,
    ProjectDescription,
    ProjectDescriptionList,
    IconSkill
)
from django.core.mail import send_mail
from .forms import ContactForm


# Renders the home page.
# 'iconskills' pulls skills with their associated pictures from the database
# 'projects' renders projects from the database
def home(request):
    context = {
        'iconskills': IconSkill.objects.all(),
        'projects': Project.objects.all().order_by('index_key')
    }
    return render(request, 'projects/home.html', context)


# Handles the backend of the contact form. This reads in the data
# from the form and then sends it to the specified email address.
# Form fields are pulled from forms.py in the projects app.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['rex.ha.mitchell@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(
                subject,
                message,
                sender,
                recipients,
                fail_silently=False)
            return render(request, 'projects/contact_success.html', {'title': 'Contact'})

    else:
        form = ContactForm()

    return render(request, 'projects/contact.html', {'form': form, 'title': 'Contact'})


# Renders the contact success page.
def contact_success(request):
    return render(request, 'projects/contact_success.html', {'title': 'Contact'})


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
def about_me(request):
    return render(request, 'projects/about_me.html', {'title': 'About'})


# Renders the resume page
def resume(request):
    return render(request, 'projects/resume.html', {'title': 'Resume'})


# Renders the checklist page. Entries and headers are stored in the database
def checklist(request):
    context = {
        'headers': CheckListHeader.objects.all().order_by('indexkey'),
        'linkheaders': LinkHeader.objects.all(),
        'title': 'Checklist'
    }
    return render(request, 'projects/project_checklist.html', context)
