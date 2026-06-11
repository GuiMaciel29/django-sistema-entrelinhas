from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]