from django.urls import path
from . import views


urlpatterns = [
    path('', views.bienvenidos, name='bienvenidos'),
    path('reserva-sala-conferencias/', views.reserva_sala_conferencias, name='reserva_sala_conferencias'),
    path('reserva-buffet/', views.reserva_buffet, name='reserva_buffet'),
    path('reserva-habitacion/', views.reserva_habitacion, name='reserva_habitacion'),
    path('mostrar-buffet/', views.mostrar_buffet, name='mostrar_buffet'),
]