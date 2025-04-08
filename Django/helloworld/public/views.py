from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from datetime import datetime




class HomeView(View):
    def get(self, request):
        fecha = datetime.now()
        return render(request, 'home.html', {'mifecha': fecha, 'classname': 'text-start', 'size': 14})
    
    def post(self, request):
        pass


def home(request):
    if (request.method == 'GET'):
        fecha = datetime.now()
        return render(request, 'home3.html', {'mifecha': fecha, 'classname': 'text-center', 'size': 14})
    elif (request.method == 'POST'):
        pass
    


    
def home1(request):
    return HttpResponse("Hola Mundo !!!")

def home2(request):
    return HttpResponse('<br /><h1 style="color:blue;">Hola Mundo !!!</h1>')