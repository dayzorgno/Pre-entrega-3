from django import forms
from .models import SalaConferencias, Buffet, Habitacion



class ReservaSalaConferenciasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=20)

class ReservaBuffetForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=20)

class ReservaHabitacionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=20)