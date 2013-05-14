__author__ = 'Marcelo'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'usuarios.views.listar_usuarios', name='listado_usuarios'),
    url(r'^ingresar/$', 'usuarios.views.ingresar_usuario', name='ingresar_usuario'),
    url(r'^editar/(\d+)/$', 'usuarios.views.editar_usuario', name='editar_usuario'),
    url(r'^eliminar/(\d+)/$', 'usuarios.views.eliminar_usuario', name='eliminar_usuario'),
    url(r'^activar/(\d+)/$', 'usuarios.views.activar_usuario', name='activar_usuario'),
)