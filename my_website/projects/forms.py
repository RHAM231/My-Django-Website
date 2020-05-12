from django import forms


# Creates the logic for the form fields on the contact form.
# 'attrs' generates html for CSS styling.
class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 'class': 'form-control'}))
    sender = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'form-control'}))
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject', 'class': 'form-control'}), max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'class': 'form-control'}))
    cc_myself = forms.BooleanField(
        required=False, label='Cc Myself')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
