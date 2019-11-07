from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.
def home(request):
    myContact = Contact()
    myContact.name = 'Anemona'
    return HttpResponse('<h1>Hello Dear</h1>')
