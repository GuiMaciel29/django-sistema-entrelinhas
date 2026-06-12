from django.db import models


class Pedido(models.Model):

    STATUS_CHOICES = [
        ('ORCAMENTO', 'Orçamento'),
        ('PRODUCAO', 'Produção'),
        ('PRONTO', 'Pronto'),
        ('ENTREGUE', 'Entregue'),
    ]

    cliente = models.CharField(
        max_length=150
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    servico = models.CharField(
        max_length=150
    )

    descricao = models.TextField(
        blank=True
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    sinal_pago = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

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

    observacoes = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def saldo(self):
        return self.valor - self.sinal_pago

    def __str__(self):
        return f"{self.cliente} - {self.servico}"


class ProdutoEstoque(models.Model):

    nome = models.CharField(
        max_length=100
    )

    quantidade = models.IntegerField(
        default=0
    )

    estoque_minimo = models.IntegerField(
        default=0
    )

    unidade = models.CharField(
        max_length=20,
        default='un'
    )

    custo_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nome


class Receita(models.Model):

    descricao = models.CharField(
        max_length=200
    )

    cliente = models.CharField(
        max_length=150,
        blank=True
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data = models.DateField()

    observacoes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.descricao


class Despesa(models.Model):

    descricao = models.CharField(
        max_length=200
    )

    categoria = models.CharField(
        max_length=100
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data = models.DateField()

    observacoes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.descricao