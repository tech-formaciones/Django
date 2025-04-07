from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def home(request):
    fecha = datetime.now()
    return render(request, 'home3.html', {'mifecha': fecha})

def home1(request):
    return HttpResponse("Hola Mundo !!!")

def home2(request):
    return HttpResponse('<br /><h1 style="color:blue;">Hola Mundo !!!</h1>')