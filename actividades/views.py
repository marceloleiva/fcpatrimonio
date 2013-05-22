# -*- coding: utf-8 -*-
from actividades.models import Actividades
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.form import UsuarioForm, UsuarioFormEdit
from usuarios.models import Usuario

from endless_pagination.decorators import page_template

from datetime import *

@page_template('page_template.html')
@login_required(login_url='/')
def actividades (request, template='index.html', extra_context=None):
    actividades = Actividades.objects.all()
    context = {
        'actividades': actividades,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))