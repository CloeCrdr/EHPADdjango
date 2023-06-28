from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname','lastname','email','subject',"message"]
        labels = {
            'firstname': _('Prénom'),
            'lastname': _('Nom'),
            'email': _('Adresse e-mail'),
            'subject': _('Sujet'),
            'message': _('Message'),
        }
