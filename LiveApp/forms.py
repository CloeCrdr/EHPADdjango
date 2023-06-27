from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    message = forms.CharField(label='Message', widget=forms.Textarea)
