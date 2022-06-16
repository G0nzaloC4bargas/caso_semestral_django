from django.shortcuts import render, redirect

from .Carrito import Carrito,guardar_carrito,eliminar,limpiar,agregar,restar
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'tienda/home.html')

def catalogo(request):
    prod=Producto.objects.all()
    data_prod = {
        'productos': prod
    }
    return render(request, 'tienda/tienda.html',data_prod)

def registro(request):
    return render(request, 'tienda/registro.html')

def login(request):
    return render(request, 'tienda/login.html')


# Llamada logica del carrito de compra
def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")