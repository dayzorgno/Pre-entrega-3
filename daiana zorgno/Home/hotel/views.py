

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SalaConferenciasForm, BuffetForm, HabitacionForm

def bienvenidos(request):
    return HttpResponse("Bienvenidos a mi hotel")

def reserva_sala_conferencias(request):
    if request.method == 'POST':
        form = SalaConferenciasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sala de conferencias reservada")
    else:
        form = SalaConferenciasForm()
    return render(request, 'hotel/reserva_sala_conferencias.html', {'form': form})


def reserva_buffet(request):
    if request.method == 'POST':
        form = ReservaBuffetForm(request.POST)
        if form.is_valid():
             form.save()
            return HttpResponse("Buffet reservado")
    else:
        form = BuffetForm()
    return render(request, 'hotel/reserva_buffet.html', {'form': form})

def reserva_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Habitación reservada")
    else:
        form = HabitacionForm()
    return render(request, 'hotel/reserva_habitacion.html', {'form': form})

from django.shortcuts import render
from .models import Buffet

def mostrar_buffet(request):
    
    buffet = Buffet.objects.latest('id')

    return render(request, 'tu_plantilla.html', {'buffet': buffet})

