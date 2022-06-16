from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('catalogo/', catalogo, name="catalogo"),
    path('Registro/', registro, name="registro"),
    path('Login/', login, name="login"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]