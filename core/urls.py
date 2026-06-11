from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )