from django import template
from django.forms.fields import CheckboxInput

register = template.Library()


# This creates logic for a custom Django template filter used in the
# contact_me.html template under projects. It checks to see if a field
# is a checkbox so that a label can be displayed just for the checkbox
# field to allow for CSS customization of the contact form.
@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, CheckboxInput)
