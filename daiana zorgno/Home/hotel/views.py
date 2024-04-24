

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservaSalaConferenciasForm, ReservaBuffetForm, ReservaHabitacionForm

def bienvenidos(request):
    return HttpResponse("Bienvenidos a mi hotel")

def reserva_sala_conferencias(request):
    if request.method == 'POST':
        form = ReservaSalaConferenciasForm(request.POST)
        if form.is_valid():
            # Procesar formulario y realizar reserva
            return HttpResponse("Sala de conferencias reservada")
    else:
        form = ReservaSalaConferenciasForm()
    return render(request, 'hotel/reserva_sala_conferencias.html', {'form': form})

def reserva_buffet(request):
    if request.method == 'POST':
        form = ReservaBuffetForm(request.POST)
        if form.is_valid():
            # Procesar formulario y realizar reserva
            return HttpResponse("Buffet reservado")
    else:
        form = ReservaBuffetForm()
    return render(request, 'hotel/reserva_buffet.html', {'form': form})

def reserva_habitacion(request):
    if request.method == 'POST':
        form = ReservaHabitacionForm(request.POST)
        if form.is_valid():
            # Procesar formulario y realizar reserva
            return HttpResponse("Habitación reservada")
    else:
        form = ReservaHabitacionForm()
    return render(request, 'hotel/reserva_habitacion.html', {'form': form})

from django.shortcuts import render
from .models import Buffet

def mostrar_buffet(request):
    
    buffet = Buffet.objects.latest('id')

    return render(request, 'tu_plantilla.html', {'buffet': buffet})

