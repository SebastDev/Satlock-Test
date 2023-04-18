from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class TipoProducto(models.Model):
    TProducto = models.CharField('Tipo del producto', max_length = 100)
    
    def __str__(self):
        return self.TProducto
    
    class Meta: 
        verbose_name = 'Tipo del producto'
        verbose_name_plural = 'Tipos de producto'
        db_table = 'tproducto'
        ordering = ['id']

class Productos(models.Model):
    NombreProducto = models.CharField('Nombre del producto', max_length = 100)
    CanActProducto = models.PositiveIntegerField('Cantidad de productos en bodega', null=True)
    PrecioProducto = models.DecimalField('Precio de venta por unidad', max_digits = 10, decimal_places = 2)
    NumProdPedidos = models.PositiveIntegerField('Número de productos por debajo del cual se debe hacer un nuevo pedido al laboratorio', null=True)
    TipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, default='')
    # Agregar foráneas
    
    def __str__(self):
        return self.NombreProducto
    
    class Meta: 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']