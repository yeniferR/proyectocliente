from django.contrib import admin

from apps.inventario.models import Producto, Inventario

# Register your models here.
admin.site.register(Inventario)
admin.site.register(Producto)
