from django.contrib import admin
from .models import Producto

# Register your models here.
# admin.site.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'name',
        'price'
    )

admin.site.register(Producto, ProductoAdmin)