from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import (
    Pedido,
    ProdutoEstoque,
    Receita,
    Despesa
)


# ===================================
# HOME
# ===================================

def home(request):
    return render(request, 'home.html')


# ===================================
# DASHBOARD
# ===================================

@login_required
def dashboard(request):

    total_receitas = (
        Receita.objects.aggregate(
            total=Sum('valor')
        )['total'] or 0
    )

    total_despesas = (
        Despesa.objects.aggregate(
            total=Sum('valor')
        )['total'] or 0
    )

    lucro = total_receitas - total_despesas

    pedidos_producao = Pedido.objects.filter(
        status='PRODUCAO'
    ).count()

    pedidos_prontos = Pedido.objects.filter(
        status='PRONTO'
    ).count()

    pedidos_entregues = Pedido.objects.filter(
        status='ENTREGUE'
    ).count()

    total_pedidos = Pedido.objects.count()

    return render(
        request,
        'dashboard.html',
        {
            'receitas': total_receitas,
            'despesas': total_despesas,
            'lucro': lucro,
            'producao': pedidos_producao,
            'prontos': pedidos_prontos,
            'entregues': pedidos_entregues,
            'total_pedidos': total_pedidos,
        }
    )


# ===================================
# PEDIDOS
# ===================================

@login_required
def lista_pedidos(request):

    pedidos = Pedido.objects.order_by('-id')

    return render(
        request,
        'pedidos/lista_pedidos.html',
        {
            'pedidos': pedidos
        }
    )


@login_required
def novo_pedido(request):

    if request.method == 'POST':

        Pedido.objects.create(
            cliente=request.POST.get('cliente'),
            telefone=request.POST.get('telefone'),
            servico=request.POST.get('servico'),
            descricao=request.POST.get('descricao'),
            valor=request.POST.get('valor'),
            sinal_pago=request.POST.get('sinal_pago') or 0,
            data_entrega=request.POST.get('data_entrega'),
            status=request.POST.get('status'),
            arte_cliente=request.FILES.get('arte_cliente')
        )

        return redirect('lista_pedidos')

    return render(
        request,
        'pedidos/novo_pedido.html'
    )


# ===================================
# ESTOQUE
# ===================================

@login_required
def estoque(request):

    produtos = ProdutoEstoque.objects.all().order_by('nome')

    return render(
        request,
        'estoque/estoque.html',
        {
            'produtos': produtos
        }
    )


@login_required
def novo_produto(request):

    if request.method == 'POST':

        ProdutoEstoque.objects.create(
            nome=request.POST.get('nome'),
            quantidade=request.POST.get('quantidade'),
            estoque_minimo=request.POST.get('estoque_minimo'),
            custo_unitario=request.POST.get('custo_unitario')
        )

        return redirect('estoque')

    return render(
        request,
        'estoque/novo_produto.html'
    )


@login_required
def editar_produto(request, id):

    produto = get_object_or_404(
        ProdutoEstoque,
        id=id
    )

    if request.method == 'POST':

        produto.nome = request.POST.get('nome')
        produto.quantidade = request.POST.get('quantidade')
        produto.estoque_minimo = request.POST.get('estoque_minimo')
        produto.custo_unitario = request.POST.get('custo_unitario')

        produto.save()

        return redirect('estoque')

    return render(
        request,
        'estoque/editar_produto.html',
        {
            'produto': produto
        }
    )


# ===================================
# RECEITAS
# ===================================

@login_required
def receitas(request):

    receitas = Receita.objects.all().order_by('-data')

    total = sum(
        receita.valor
        for receita in receitas
    )

    return render(
        request,
        'financeiro/receitas.html',
        {
            'receitas': receitas,
            'total': total
        }
    )


@login_required
def nova_receita(request):

    if request.method == 'POST':

        Receita.objects.create(
            descricao=request.POST.get('descricao'),
            valor=request.POST.get('valor'),
            data=request.POST.get('data'),
            cliente=request.POST.get('cliente')
        )

        return redirect('receitas')

    return render(
        request,
        'financeiro/nova_receita.html'
    )


# ===================================
# DESPESAS
# ===================================

@login_required
def despesas(request):

    despesas = Despesa.objects.all().order_by('-data')

    total = sum(
        despesa.valor
        for despesa in despesas
    )

    return render(
        request,
        'financeiro/despesas.html',
        {
            'despesas': despesas,
            'total': total
        }
    )


@login_required
def nova_despesa(request):

    if request.method == 'POST':

        Despesa.objects.create(
            descricao=request.POST.get('descricao'),
            valor=request.POST.get('valor'),
            data=request.POST.get('data'),
            categoria=request.POST.get('categoria')
        )

        return redirect('despesas')

    return render(
        request,
        'financeiro/nova_despesa.html'
    )