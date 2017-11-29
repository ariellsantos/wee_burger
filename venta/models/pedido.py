# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    """Model definition for Pedido."""

    ESTATUS = (
        ('cl', 'Colocado'),
        ('p', 'En Proceso'),
        ('t', 'Terminado'),
        ('e', 'Entregado'),
        ('c', 'Cancelado')
    )

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    total_pagar = models.DecimalField(max_digits=11, decimal_places=2)
    estatus = models.CharField(max_length=10, choices=ESTATUS, default="colocado")

    

    class Meta:
        """Meta definition for Pedido."""

        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __unicode__(self):
        """Unicode representation of Pedido."""
        return "Cliente: {} Fecha {}".format(self.cliente, self.fecha)
