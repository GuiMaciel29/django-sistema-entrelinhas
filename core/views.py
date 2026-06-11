from django.shortcuts import render
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
    return render(request, 'pedidos/novo_pedido.html')