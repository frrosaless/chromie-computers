from django.contrib import admin
from .models import Categoria, Marca, Producto, Cliente, UserProfile, Venta, DetalleVenta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(UserProfile)
