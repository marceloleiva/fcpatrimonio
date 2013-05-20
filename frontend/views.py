#encoding:utf-8

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from form import LoginForm


def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')

    login_form = LoginForm(request.POST or None)
    form_login = login_form.is_valid()

    if form_login:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, 'Bienvenido ' + request.user.get_short_name() + '.')
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, 'Tu nombre de usuario o contraseña es incorrecto.')

    context = {
        'login_form': login_form,
    }
    return render_to_response('login.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def home(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
