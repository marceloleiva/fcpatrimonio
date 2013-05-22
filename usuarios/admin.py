__author__ = 'Marcelo'

from django.contrib import admin
from usuarios.models import Usuario, Perfil, Filial, SubGerencia, Unidad
from actividades.models import Actividades


admin.site.register(Filial)
admin.site.register(SubGerencia)
admin.site.register(Unidad)
admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Actividades)
