from django.db import models

class Juegos(models.Model):
    nombre = models.CharField(max_length=30)
    subnombre = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    fecha = models.IntegerField
    imagen = models.ImageField
