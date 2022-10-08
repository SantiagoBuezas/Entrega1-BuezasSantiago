from django.contrib import admin
from Blog.models import Autor, Articulo, Seccion

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Seccion)
