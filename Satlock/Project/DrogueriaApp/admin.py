from django.contrib import admin
from .models import Productos
from .models import TipoProducto

admin.site.register(Productos)
admin.site.register(TipoProducto)