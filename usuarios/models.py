#encoding:utf-8

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from tastypie.models import create_api_key

GENERO = (
    ('M', 'Hombre'),
    ('F', 'Mujer'),
)

NOW = timezone.now()


class Filial(models.Model):
    codigo_interno = models.CharField('Codigo Interno', max_length=10, unique=True)
    nombre = models.CharField('Nombre', max_length=40)

    def __unicode__(self):
        return self.nombre


class SubGerencia(models.Model):
    filial = models.ForeignKey(Filial)
    codigo_interno = models.CharField('Codigo Interno', max_length=10, unique=True)
    nombre = models.CharField('Nombre', max_length=40)

    def __unicode__(self):
        return self.nombre


class Unidad(models.Model):
    subgerencia = models.ForeignKey(SubGerencia)
    codigo_interno = models.CharField('Codigo Interno', max_length=10, unique=True)
    nombre = models.CharField('Nombre', max_length=40)

    def __unicode__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField('Nombre', max_length=50)
    apellido_paterno = models.CharField('Apellido paterno', max_length=50)
    apellido_materno = models.CharField('Apellido materno', max_length=50, blank=True)
    rut = models.CharField('RUT', max_length=10, unique=True)
    unidad = models.ForeignKey(Unidad)
    subgerencia = models.ForeignKey(SubGerencia)
    filial = models.ForeignKey(Filial)
    genero = models.CharField('Genero', max_length=1, choices=GENERO, blank=True)
    celular = models.PositiveIntegerField('Celular', max_length=10, null=True)
    imei = models.CharField('IMEI', max_length=30, blank=True)
    rol = models.IntegerField('ROL', max_length=1)

    def __unicode__(self):
        return self.nombre


models.signals.post_save.connect(create_api_key, sender=User)