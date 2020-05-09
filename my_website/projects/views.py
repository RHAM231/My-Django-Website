from django.shortcuts import render, redirect
from . models import (
    Project,
    CheckListHeader,
    LinkHeader,
    ProjectSummary,
    ProjectSummaryList,
    ProjectDescription,
    ProjectDescriptionList,
    PortfolioInfo,
    TestObject,
    PortfolioSkill,
    Logo,
    IconSkill
)
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic import (
    ListView,
    DetailView
)


def home(request):
    me = PortfolioInfo.objects.get()
    context = {
        'iconskills': IconSkill.objects.all(),
        'projects': Project.objects.all().order_by('index_key'),
        'mybackground': me.background
    }
    return render(request, 'projects/home.html', context)


# Handles the backend of the contact form. This reads in the data
# from the form and then sends it to the specified email address.
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


def contact_success(request):
    return render(request, 'projects/contact_success.html', {'title': 'Contact'})


def portfolio_project(request):
    logo = Logo.objects.get()
    context = {
        'logo': logo.image,
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


def about_me(request):
    me = PortfolioInfo.objects.get()
    myskills = PortfolioSkill.objects.all()
    context = {
        'myimage': me.image,
        'myskills': myskills,
        'title': 'About'
    }
    return render(request, 'projects/about_me.html', context)


def resume(request):
    return render(request, 'projects/resume.html', {'title': 'Resume'})


def checklist(request):
    context = {
        'headers': CheckListHeader.objects.all().order_by('indexkey'),
        'linkheaders': LinkHeader.objects.all(),
        'title': 'Checklist'
    }
    # stuff2 = CheckListEntry.objects.filter(name__contains='Keep')

    return render(request, 'projects/project_checklist.html', context)


# class CheckListView(ListView):
#     # queryset = CheckListHeader.objects.all()
#     context_object_name = 'headers'
#     model = CheckListHeader
#     template_name = 'projects/project_checklist.html'
