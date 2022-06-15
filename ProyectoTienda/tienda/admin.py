from django.contrib import admin
from .models import producto,user,venta,venta_producto, Contacto

# Register your models here.

admin.site.register(producto)
admin.site.register(user)
admin.site.register(venta)
admin.site.register(venta_producto)
admin.site.register(Contacto)