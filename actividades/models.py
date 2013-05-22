# -*- coding: utf-8 -*-

from django.db import models
from usuarios.models import Usuario


class Actividades(models.Model):
    usuario = models.ForeignKey(Usuario)
    fecha_actividad = models.DateField()
    inicio_actividad = models.TimeField()
    termino_actividad = models.TimeField()
    estado = models.BooleanField(default=False)
    latitud = models.CharField(max_length=25)
    longitud = models.CharField(max_length=25)