from django.shortcuts import render
from django.core.mail import send_mail
from . forms import ContactForm


# def contact_me_test(request):
#     return render(request, 'contact/contact_form.html')


# Handles the backend of the contact form. This reads in the data
# from the form and then sends it to the specified email address.
# Form fields are pulled from forms.py in the projects app.
def contact_me(request):
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
            return render(request, 'contact/contact_form_success.html', {'title': 'Contact'})

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form, 'title': 'Contact'})


# Renders the contact success page upon successful completion of the form.
# def contact_success(request):
#     return render(request, 'contact/contact_form_success.html', {'title': 'Contact'})
