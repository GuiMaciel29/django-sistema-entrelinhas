from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),
]