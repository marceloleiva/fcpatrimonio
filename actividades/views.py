# -*- coding: utf-8 -*-
from actividades.models import Actividades
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.form import UsuarioForm, UsuarioFormEdit
from usuarios.models import PerfilUsuario

from datetime import *

@login_required(login_url='/')
def actividades (request):
    actividades = Actividades.objects.all()

    for actividad in actividades:
        inicio = actividad.inicio_actividad
        termino = actividad.termino_actividad
        print inicio

    context = {
        'actividades': actividades,
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))