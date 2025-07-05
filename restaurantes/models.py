from django.db import models
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    fecha_hora = models.DateTimeField()
    comensales = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.usuario.nombre} en {self.restaurante.nombre}"
