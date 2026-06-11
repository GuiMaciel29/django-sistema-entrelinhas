from django.db import models

class Pedido(models.Model):

    STATUS_CHOICES = [
        ('ORCAMENTO', 'Orçamento'),
        ('PRODUCAO', 'Produção'),
        ('PRONTO', 'Pronto'),
        ('ENTREGUE', 'Entregue'),
    ]

    cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    servico = models.CharField(max_length=100)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    sinal_pago = models.DecimalField(max_digits=10, decimal_places=2)

    data_entrega = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ORCAMENTO'
    )

    arte_cliente = models.FileField(
        upload_to='artes/',
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente