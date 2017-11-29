# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto import Producto
from pedido import Pedido

class ProductosPedido(models.Model):
    """Model definition for ProductosPedido."""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10 , decimal_places=2)
    cantidad = models.IntegerField()
    

    class Meta:
        """Meta definition for ProductosPedido."""

        verbose_name = 'ProductosPedido'
        verbose_name_plural = 'ProductosPedidos'

    def __unicode__(self):
        """Unicode representation of ProductosPedido."""
        return "Pedido: {}  Producto: {}".format(self.pedido, self.producto)
