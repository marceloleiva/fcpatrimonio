__author__ = 'Marcelo'

from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from models import Actividades


class UsuariosResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()

        excludes = [
            'password',
            'is_staff',
            'is_superuser',
            'is_admin',
            'is_active',
            'email',
        ]


class ActividadesResource(ModelResource):
    usuario = fields.ForeignKey(UsuariosResource, 'usuario')

    class Meta:
        queryset = Actividades.objects.all()
        resource_name = 'actividades'
        allowed_methods = ['post']
        authentication = ApiKeyAuthentication()
