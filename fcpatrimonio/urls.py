from actividades.models import Actividades
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'frontend.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
                       url(r'^home/$', 'actividades.views.actividades', name='home'),

                       url(r'^administrar/usuarios/', include('usuarios.urls', namespace='usuarios')),
)
