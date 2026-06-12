from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    endereco = models.TextField(blank=True)

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='servicos/')
    preco_base = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
class Pedido(models.Model):

    STATUS = [
        ('ORCAMENTO','Orçamento'),
        ('PRODUCAO','Produção'),
        ('PRONTO','Pronto'),
        ('ENTREGUE','Entregue')
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE
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

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    arte_cliente = models.FileField(
        upload_to='artes/'
    )

    data_entrega = models.DateField()

class ProdutoEstoque(models.Model):

    nome = models.CharField(max_length=100)

    quantidade = models.IntegerField()

    estoque_minimo = models.IntegerField()

    custo_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nome

class Despesa(models.Model):

    descricao = models.CharField(max_length=200)

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data = models.DateField()

    categoria = models.CharField(
        max_length=100
    )

    