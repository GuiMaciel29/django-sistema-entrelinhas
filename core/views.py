from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from django.contrib.auth.decorators import login_required
from .models import ProdutoEstoque


@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()

    return render(
        request,
        'pedidos/lista_pedidos.html',
        {'pedidos': pedidos}
    )

@login_required
def novo_pedido(request):

    if request.method == 'POST':

        Pedido.objects.create(
            cliente=request.POST.get('cliente'),
            telefone=request.POST.get('telefone'),
            servico=request.POST.get('servico'),
            valor=request.POST.get('valor'),
            sinal_pago=request.POST.get('sinal_pago'),
            data_entrega=request.POST.get('data_entrega'),
            status=request.POST.get('status'),
            arte_cliente=request.FILES.get('arte_cliente')
        )

        return redirect('lista_pedidos')

    return render(request, 'pedidos/novo_pedido.html')

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    pedidos = Pedido.objects.order_by('-id')[:10]

    return render(
        request,
        'dashboard.html',
        {'pedidos': pedidos}
    )
@login_required
def estoque(request):

    produtos = ProdutoEstoque.objects.all()

    return render(
        request,
        'estoque/estoque.html',
        {'produtos': produtos}
    )

@login_required
def novo_produto(request):

    if request.method == 'POST':

        ProdutoEstoque.objects.create(
            nome=request.POST['nome'],
            quantidade=request.POST['quantidade'],
            estoque_minimo=request.POST['estoque_minimo'],
            custo_unitario=request.POST['custo_unitario']
        )

        return redirect('estoque')

    return render(
        request,
        'estoque/novo_produto.html'
    )

@login_required
def novo_produto(request):

    if request.method == 'POST':

        ProdutoEstoque.objects.create(
            nome=request.POST['nome'],
            quantidade=request.POST['quantidade'],
            estoque_minimo=request.POST['estoque_minimo'],
            custo_unitario=request.POST['custo_unitario']
        )

        return redirect('estoque')

    return render(
        request,
        'estoque/novo_produto.html'
    )

def editar_produto(request, id):

    produto = get_object_or_404(
        ProdutoEstoque,
        id=id
    )

    if request.method == 'POST':

        produto.nome = request.POST['nome']
        produto.quantidade = request.POST['quantidade']
        produto.estoque_minimo = request.POST['estoque_minimo']
        produto.custo_unitario = request.POST['custo_unitario']

        produto.save()

        return redirect('estoque')

    return render(
        request,
        'estoque/editar_produto.html',
        {'produto': produto}
    )