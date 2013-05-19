__author__ = 'Marcelo'

from django.contrib import admin
from usuarios.models import PerfilUsuario
from actividades.models import Actividades

admin.site.register(PerfilUsuario)
admin.site.register(Actividades)
