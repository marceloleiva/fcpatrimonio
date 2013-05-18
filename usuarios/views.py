# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.form import UsuarioForm, UsuarioFormEdit
from usuarios.models import PerfilUsuario

@login_required(login_url='/')
def ingresar_usuario (request):
    usuario_form = UsuarioForm(request.POST or None)
    form_usuario = usuario_form.is_valid()
    if form_usuario:
        usuario = usuario_form.save(commit=False)
        usuario.set_password(usuario_form.cleaned_data['password'])
        usuario.save()
        messages.success(request,'El usuario se ingresó correctamente.')
        return HttpResponseRedirect('/home')
    context = {
        'usuario_form' : usuario_form,
    }
    return render_to_response('usuarios/ingresar_usuarios.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editar_usuario(request, object_id):
    usuario = PerfilUsuario.objects.get(id=object_id)
    print usuario
    if request.method == 'POST':
        recepcionista_form = UsuarioFormEdit(request.POST, instance=usuario)
        if recepcionista_form.is_valid():
            recepcionista_form.save()
            messages.success(request,'El usuario se actualizó correctamente.')
            return HttpResponseRedirect('/home')
    else:
        usuario_form = UsuarioFormEdit(instance=usuario)
    context = {
        'usuario_form' : usuario_form,
    }
    return render_to_response("usuarios/editar_usuarios.html", context,  context_instance=RequestContext(request))


@login_required(login_url='/')
def listar_usuarios(request):
    lista = PerfilUsuario.objects.all()
    context = {
        'usuarios' : lista,
    }
    return render_to_response('usuarios/listado_usuarios.html',  context, context_instance=RequestContext(request))


@login_required(login_url='/')
def eliminar_usuario(request, id):
    try:
        usuario = PerfilUsuario.objects.get(id=id)
        if usuario.is_active:
            usuario.is_active = False
            usuario.save()
            messages.success(request,'El usuario fue eliminado correctamente.')
            return HttpResponseRedirect('/administrar/usuarios')
        else:
            messages.success(request,'El usuario no existe en el sistema.')
            return HttpResponseRedirect('/administrar/usuarios')
    except:
        messages.success(request,'El usuario, no se puede eliminar.')
        return HttpResponseRedirect('/administrar/usuarios')

@login_required(login_url='/')
def activar_usuario(request, id):
    usuario = PerfilUsuario.objects.get(pk=id)
    print usuario.is_active
    try:
        usuario = PerfilUsuario.objects.get(pk=id)
        if usuario.is_active:
            messages.success(request,'El usuario ya se encuentra activo en el sistema.')
            return HttpResponseRedirect('/administrar/usuarios')
        else:
            usuario.is_active = True
            usuario.save()
            messages.success(request,'El fue activado correctamente.')
            return HttpResponseRedirect('/administrar/usuarios')
    except:
        messages.success(request,'El usuario no se puede activar.')
        return HttpResponseRedirect('/administrar/usuarios')
