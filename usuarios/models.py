#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User


GENERO = (
    ('M', 'Hombre'),
    ('F', 'Mujer'),
    )

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO, blank=True)
    telefono = models.PositiveIntegerField(max_length=10, blank=True)
    celular = models.PositiveIntegerField(max_length=10, blank=True)
    mail = models.EmailField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"