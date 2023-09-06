from django.contrib import admin
from django.urls import path
from FINECAP.views import index, reserva_criar, reserva_editar, reserva_remover, reserva_listar, reserva_detalhe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('reserva/', reserva_criar, name='reserva_criar'),
    path('reserva/editar/<int:id>/', reserva_editar, name='reserva_editar'),
    path('reserva/remover/<int:id>/', reserva_remover, name='reserva_remover'),
    path('reserva/listar/', reserva_listar, name='reserva_listar'),
    path('reserva/detalhe/<int:id>/', reserva_detalhe, name='reserva_detalhe')
]