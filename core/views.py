from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pedido

def home(request):
    return HttpResponse("Olá, Django!")

def lista_pedidos(request):
    pedidos = Pedido.objects.all()

    return render(
        request,
        'pedidos/lista_pedidos.html',
        {'pedidos': pedidos}
    )
def novo_pedido(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        Pedido.objects.create(
            cliente=cliente,
            produto=produto,
            quantidade=quantidade
        )

        return redirect('lista_pedidos')

    return render(request, 'pedidos/novo_pedido.html')