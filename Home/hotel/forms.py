from django import forms
from .models import SalaConferencias, Buffet, Habitacion

class SalaConferenciasForm(forms.ModelForm):
    class Meta:
        model = SalaConferencias
        fields = ['nombre', 'capacidad']

class BuffetForm(forms.ModelForm):
    class Meta:
        model = Buffet
        fields = ['horario', 'menu']  # Cerré la comilla simple aquí

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['horario_admision', 'camas_disponibles'] 