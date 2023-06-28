from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

from django.core.mail import EmailMessage
from .forms import ContactForm, ServiceForm
from .models import Contact, Service


# Create your views here.
def home(request):
    return render(request, "LiveApp/home.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            
            # Envoi de l'e-mail
            subject = f'Nouveau message de contact: {subject}'
            body = f'Nom: {lastname} {firstname}, \nAdresse e-mail: {email}\nMessage: {message}'
            to_email = 'admin@ehpadexample.com'  # Adresse e-mail de l'administrateur du site
            email_message = EmailMessage(subject, body, to=[to_email])
            email_message.send()
            
            # Redirection vers une page de confirmation ou affichage d'un message de réussite
            return render(request, 'LiveApp/success.html')
    else:
        form = ContactForm()
    
    return render(request, 'LiveApp/contact.html', {'form': form})

def about(request):
    return render(request, 'LiveApp/about.html') 

def services(request):
    services = Service.objects.all()
    return render(request, 'LiveApp/services.html', {'services': services}) 

def success(request):
    return render(request, 'LiveApp/success.html') 

def admin(request):
    services = Service.objects.all()
    return render(request, 'LiveApp/admin/service_manage.html', {'services': services}) 

def delete_service(request,id):
    if request.method == "GET":
        service = Service.objects.get(id=id)
        service.delete()   
    return redirect('LiveApp:admin_ehpad')

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('LiveApp:admin_ehpad')
    else:
        form = ServiceForm()
    return render(request, 'LiveApp/admin/service_create.html', {'form' :form})
    
def update_service(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('LiveApp:admin_ehpad')
    
    else:
        form = ServiceForm(instance=service)

    return render(request, 'LiveApp/admin/service_update.html', {'form': form, 'service': service})