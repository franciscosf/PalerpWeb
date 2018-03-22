from django.shortcuts import render
from django.http import HttpResponse

from apps.productos.models import Producto
# Create your views here.

def tienda_view(request):
	productos = Producto.objects.all()
	return render(request, 'views/tienda.html', {'productos':productos})

def prueba(request):
	return render(request, 'views/prueba.html')
