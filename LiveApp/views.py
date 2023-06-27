from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "LiveApp/home.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Envoi de l'e-mail
            subject = 'Nouveau message de contact'
            body = f'Nom: {name}\nAdresse e-mail: {email}\nMessage: {message}'
            to_email = 'admin@example.com'  # Adresse e-mail de l'administrateur du site
            email_message = EmailMessage(subject, body, to=[to_email])
            email_message.send()
            
            # Redirection vers une page de confirmation ou affichage d'un message de réussite
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    
    return render(request, 'LiveApp/contact.html', {'form': form})

def about(request):
    return render(request, 'LiveApp/about.html') 

def services(request):
    return render(request, 'LiveApp/services.html') 