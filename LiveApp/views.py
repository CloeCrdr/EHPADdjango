from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return render(request, "LiveApp/home.html")
