from django.contrib import admin
from django.urls import path
from FINECAP import views

app_name = "FINECAP"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='index'),
    path('reserva/', views.reserva_criarView.as_view(), name='reserva_criar'),
    path('reserva/editar/<int:pk>/', views.reserva_editarView.as_view(), name='reserva_editar'),
    path('reserva/remover/<int:pk>/', views.reserva_removerView.as_view(), name='reserva_remover'),
    path('reserva/listar/', views.reserva_listarView.as_view(), name='reserva_listar'),
    path('reserva/detalhe/<int:pk>/', views.reserva_detalheView.as_view(), name='reserva_detalhe'),
    path('stand/', views.stand_criarView.as_view(), name='stand_criar'),
    path('stand/editar/<int:pk>/', views.stand_editarView.as_view(), name='stand_editar'),
    path('stand/remover/<int:pk>/', views.stand_removerView.as_view(), name='stand_remover'),
    path('stand/listar/', views.stand_listarView.as_view(), name='stand_listar'),
    path('stand/detalhe/<int:pk>/', views.stand_detalheView.as_view(), name='stand_detalhe'),
]