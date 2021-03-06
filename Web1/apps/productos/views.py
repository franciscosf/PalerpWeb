from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from apps.productos.models import Producto
from apps.productos.models import Compra
from apps.productos.forms import CompraForm
# Create your views here.

def formatIntegerWithZeros(n, zeros):
	lenN = len(str(n))
	res = ''
	for a in range(zeros - lenN):
		res += '0'

	return '{0}{1}'.format(res, n)

def tienda_view(request):
	if request.method == 'POST':
		form = CompraForm(request.POST)
		tabladetalle = form.data['tabladetalle']
		importe = form.data['importe']
		cliente = User.objects.get(id = form.data['cliente'])
		nitems = form.data['nitems']

		q = Compra(tabladetalle = tabladetalle, importe = importe, cliente = cliente, nitems = nitems)
		q.save()
		idq = q.id
		print(idq)
		n1 = idq // 100000
		n2 = idq % 100000
		q.codigo = "C{0}P{1}".format(formatIntegerWithZeros(n1,3),

		formatIntegerWithZeros(n2,5))
		q.save()

		return render(request, 'views/formToPayToPeru.html', {'user': cliente, 'compra': q, 'RUCPalerp': '20491228297' })
	else:
		form = CompraForm()
	productos = Producto.objects.all()
	return render(request, 'views/tienda.html', {'productos':productos, 'form': form})

def prueba(request):
	return render(request, 'views/prueba.html')
