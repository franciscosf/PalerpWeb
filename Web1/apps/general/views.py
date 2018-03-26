from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from apps.general.forms import PosibleClienteForm

# Create your views here.

def index_view(request):
    if request.method == 'POST':
        form = PosibleClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = PosibleClienteForm()

    return render(request, 'views/index.html', {'form': form})

def productos_view(request):
    return render(request, 'views/productos.html')

def nosotros_view(request):
    return render(request, 'views/nosotros.html')

def contactanos_view(request):
    return render(request, 'views/contactanos.html')
