from django.contrib import admin
from .models import Producto,user,venta, Contacto

# Register your models here.

admin.site.register(Producto)
admin.site.register(user)
admin.site.register(venta)
admin.site.register(Contacto)