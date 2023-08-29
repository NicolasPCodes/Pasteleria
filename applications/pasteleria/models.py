from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Producto(models.Model):
    codigo = models.CharField('Codigo',primary_key=True, max_length=10)
    name = models.CharField('Nombre', max_length=60)
    price = models.IntegerField('Precio')
    stock = models.IntegerField('Stock')
    image = models.ImageField(upload_to='producto', blank=True, null=True)
    description = RichTextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.codigo) + '-' + self.name 