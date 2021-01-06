from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from . forms import ContactForm


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_context = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['sender'],
                'message': form.cleaned_data['message'],
            }
            html_content = render_to_string('contact/contact_email.html', email_context)
            plain_message = strip_tags(html_content)
            from_email = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['rex.ha.mitchell@gmail.com']

            if cc_myself:
                recipients.append(from_email)
            send_mail(subject, plain_message, from_email, recipients,
                      fail_silently=False, html_message=html_content)

            return render(request, 'contact/contact_form_success.html', {'title': 'Contact'})

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form, 'title': 'Contact'})
