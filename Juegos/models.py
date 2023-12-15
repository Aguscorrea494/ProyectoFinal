from django.db import models
import datetime

class Juegos(models.Model):
    nombre = models.CharField(max_length=30)
    subnombre = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=200)
    autor = models.CharField(max_length=30)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    imagen = models.ImageField

    def __str__(self):
        return (self.nombre)


class Mensajes(models.Model):
    pass