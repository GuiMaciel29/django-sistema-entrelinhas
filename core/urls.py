from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # PEDIDOS
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),

    # ESTOQUE
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/novo/', views.novo_produto, name='novo_produto'),
    path('estoque/editar/<int:id>/', views.editar_produto, name='editar_produto'),

    # FINANCEIRO
    path('receitas/',views.receitas,name='receitas'),
    path('receitas/nova/',views.nova_receita,name='nova_receita'),
    path('despesas/',views.despesas,name='despesas'),
    path('despesas/nova/',views.nova_despesa,name='nova_despesa'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )