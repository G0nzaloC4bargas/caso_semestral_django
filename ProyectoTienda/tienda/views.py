from django.shortcuts import render
from .models import user, producto, venta, venta_producto
from .forms import ContactoForm
# Create your views here.
def home(request):
    return render(request, 'tienda/home.html')

def catalogo(request):
    prod=producto.objects.all()
    data_prod = {
        'productos': prod
    }
    return render(request, 'tienda/catalogo.html',data_prod)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'tienda/contacto.html', data)

def registro(request):
    return render(request, 'tienda/registro.html')

def login(request):
    return render(request, 'tienda/login.html')
