from django.shortcuts import render
from django.http import HttpResponseRedirect

from apps.general.forms import PosibleClienteForm

# Create your views here.

def index_view(request):
    print('Hi')
    if request.method == 'POST':
        form = PosibleClienteForm(request.POST)
        print('POST')
        print(form)
        if form.is_valid():
            # <process form cleaned data>
            print('Valid')
            return HttpResponseRedirect('/success/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PosibleClienteForm()

    return render(request, 'views/index.html', {'form': form})

def productos_view(request):
    return render(request, 'views/productos.html')

def nosotros_view(request):
    return render(request, 'views/nosotros.html')

def contactanos_view(request):
    return render(request, 'views/contactanos.html')
