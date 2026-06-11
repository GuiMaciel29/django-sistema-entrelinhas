from django.db import models

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.produto}"