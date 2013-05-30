# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.form import UserForm, PerfilForm, PerfilFormEdit
from usuarios.models import Perfil

@login_required(login_url='/')
def ingresar_usuario (request):
    user_form = UserForm(request.POST or None)
    perfil_form = PerfilForm(request.POST or None)
    form_usuario = user_form.is_valid()
    form_perfil = perfil_form.is_valid()

    if form_usuario and form_perfil:
        new_user = User.objects.create_user(user_form.cleaned_data['username'], '', user_form.cleaned_data['password'])
        new_user.is_active = True
        new_user.is_staff = False
        new_user.is_superuser = False
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        perfil = perfil_form.save(commit=False)
        perfil.usuario = new_user
        perfil.save()
        messages.success(request,'El usuario se ingresó correctamente.')
        return HttpResponseRedirect('/administrar/usuarios')
    context = {
        'perfil_form' : perfil_form,
        'user_form' : user_form,
    }
    return render_to_response('usuarios/ingresar_usuarios.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editar_usuario(request, object_id):
    usuario = Perfil.objects.get(id=object_id)
    print usuario
    if request.method == 'POST':
        recepcionista_form = PerfilFormEdit(request.POST, instance=usuario)
        if recepcionista_form.is_valid():
            recepcionista_form.save()
            messages.success(request,'El usuario se actualizó correctamente.')
            return HttpResponseRedirect('/administrar/usuarios')
    else:
        usuario_form = PerfilFormEdit(instance=usuario)
    context = {
        'usuario_form' : usuario_form,
    }
    return render_to_response("usuarios/editar_usuarios.html", context,  context_instance=RequestContext(request))


@login_required(login_url='/')
def listar_usuarios(request):
    lista = Perfil.objects.all()
    context = {
        'usuarios' : lista,
    }
    return render_to_response('usuarios/listado_usuarios.html',  context, context_instance=RequestContext(request))


@login_required(login_url='/')
def eliminar_usuario(request, id):
    try:
        usuario = User.objects.get(id=id)
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
    usuario = User.objects.get(pk=id)
    try:
        usuario = User.objects.get(pk=id)
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
