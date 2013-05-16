# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from usuarios.form import UserForm, UsuarioForm, UsuarioFormEdit
from usuarios.models import PerfilUsuario

@login_required(login_url='/')
def ingresar_usuario (request):
    user_form = UserForm(request.POST or None)
    usuario_form = UsuarioForm(request.POST or None)
    form_user = user_form.is_valid()
    form_usuario = usuario_form.is_valid()
    if form_user and form_usuario:
        new_user = User.objects.create_user(user_form.cleaned_data['username'], '', user_form.cleaned_data['password'])
        new_user.is_active = True
        new_user.is_staff = False
        new_user.is_superuser = False
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        usuario = usuario_form.save(commit=False)
        usuario.user = new_user
        usuario.save()
        messages.success(request,'El usuario se ingresó correctamente.')
        return HttpResponseRedirect('/home')
    context = {
    'user_form' : user_form,
    'usuario_form' : usuario_form,
    }
    return render_to_response('usuarios/ingresar_usuarios.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def editar_usuario(request, object_id):
    usuario = PerfilUsuario.objects.get(user=object_id)
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
    'usuario ' : usuario.nombre ,
    'usuario_form' : usuario_form,
    }
    return render_to_response("usuarios/editar_usuarios.html", context,  context_instance=RequestContext(request))


@login_required(login_url='/')
def listar_usuarios(request):
    lista = PerfilUsuario.objects.all()
    context = {
    'usuarios'	:	lista,
    }
    return render_to_response('usuarios/listado_usuarios.html',  context, context_instance=RequestContext(request))


@login_required(login_url='/')
def eliminar_usuario(request, id):
    try:
        usuario = PerfilUsuario.objects.get(id = id)
        if usuario.user.is_active == True:
            usuario.user.is_active = False
            usuario.user.save()
            messages.success(request,'El usuario fue eliminado correctamente.')
            return HttpResponseRedirect('/usuarios')
        else:
            messages.success(request,'El usuario no existe en el sistema.')
            return HttpResponseRedirect('/usuarios')
    except:
        messages.success(request,'El no existe, no se puede eliminar.')
        return HttpResponseRedirect('/usuarios')

@login_required(login_url='/')
def activar_usuario(request, id):
    try:
        usuario = PerfilUsuario.objects.get(id = id)
        if usuario.user.is_active == False:
            usuario.user.is_active = True
            usuario.user.save()
            messages.success(request,'El fue activado correctamente.')
            return HttpResponseRedirect('/usuarios')
        else:
            messages.success(request,'El usuario no existe en el sistema.')
            return HttpResponseRedirect('/usuarios')
    except:
        messages.success(request,'El no existe, no se puede eliminar.')
        return HttpResponseRedirect('/usuarios')
