from django.contrib import admin
from .models import Publicacion, Cliente, Producto

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Publicacion)
# Register your models here.
