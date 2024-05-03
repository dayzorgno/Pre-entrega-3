from django import forms
from .models import SalaConferencias, Buffet, Habitacion



class SalaConferenciasForm(forms.ModelForm):
    class Meta:
        model = SalaConferencias
        fields = ['nombre', 'capacidad']

class BuffetForm(forms.Form):
    class Meta:
        model = Buffet
        fields = ['horario, 'menu']

class HabitacionForm(forms.Form):
    class Meta:
        model = Buffet
        fields = ['horario_admision, 'camas_disponibles']