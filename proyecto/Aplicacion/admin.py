from django.contrib import admin

from Aplicacion.models import Categoria, Cliente, Curso, Proveedores

# Register your models here.

admin.site.register(Curso)

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Proveedores)