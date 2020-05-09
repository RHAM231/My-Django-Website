from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    sender = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}), max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))
    cc_myself = forms.BooleanField(required=False, label='Cc Myself')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


# class CheckListForm(forms.Form):
#     general = forms.Label('General')


athlete_list = ['1', '2', '3']
