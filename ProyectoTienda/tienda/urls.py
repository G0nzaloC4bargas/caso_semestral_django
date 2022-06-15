from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('catalogo/', catalogo, name="catalogo"),
    path('Registro/', registro, name="registro"),
    path('Login/', login, name="login"),
    path('Contacto/', contacto, name="contacto"),
]