
from django.db import models

class SalaConferencias(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Buffet(models.Model):
    horario = models.CharField(max_length=100)
    menu = models.TextField()

    def __str__(self):
        return self.horario

    def save(self, *args, **kwargs):
        # Actualizar el menú con los elementos requeridos si no se proporcionan previamente
        if not self.menu:
            self.menu = "Fideos, Pollo, Asado, Ensalada"
        super().save(*args, **kwargs)

class Habitacion(models.Model):
    horario_admision = models.CharField(max_length=100)
    camas_disponibles = models.IntegerField(choices=[(2, 'Dos camas'), (4, 'Cuatro camas')])

    def __str__(self):
        return self.horario_admision

