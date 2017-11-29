# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from categoria import Categoria

class Producto(models.Model):
    """Model definition for Producto."""

    
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto_producto = models.ImageField(upload_to='imagen_producto/', blank=True, null=True)

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        """Unicode representation of Producto."""
        return self.nombre
