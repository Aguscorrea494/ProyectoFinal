from django.contrib.auth.models import User
from django.db import models
import datetime

class Juegos(models.Model):
    nombre = models.CharField(max_length=30)
    plataforma = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    autor = models.CharField(max_length=30)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    imagen = models.ImageField()

    def __str__(self):
        return (self.nombre)


class Comentarios(models.Model):
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=300)
    fecha = models.DateTimeField(default=datetime.datetime.now())