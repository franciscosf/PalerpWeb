from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, 'index1.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def nosotros_view(request):
    return render(request, 'views/nosotros.html')

def productos_view(request):
    return render(request, 'views/productos.html') 

def servicios_view(request):
    return render(request, 'views/servicios.html')

def contactanos_view(request):
    return render(request, 'views/contactanos.html')