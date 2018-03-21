from django.shortcuts import render
from django.http import HttpResponse

from apps.productos.models import Producto
# Create your views here.

def productos_view(request):
	productos = Producto.objects.all()
	return render(request, 'views/productos.html', {'productos':productos})

def prueba(request):
	return render(request, 'views/prueba.html')
