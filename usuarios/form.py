# -*- coding: utf-8 -*-
from bootstrap_toolkit.widgets import BootstrapDateInput

__author__ = 'Marcelo'

import re
from django import forms
from django.contrib.auth.models import User
from models import Perfil


ROLES = [
    (1, 'Consultor'),
    (2, 'Guarda bosques'),
    (3, 'Jefe de area'),
    (4, 'Administrador'),
]


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="", min_length= 6, max_length= 15)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), min_length=6, max_length=15, help_text="")

    class Meta:
        model = User
        fields = ('username', 'password')


class PerfilForm(forms.ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ej: 11111111-1'}), min_length=8, max_length=10)
    celular = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Solo Números'}), min_length=8, max_length=8)
    rol = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect())

    class Meta:
        model = Perfil
        exclude = ['usuario']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if re.match('([0-9]+-[0-9kK])', rut):
            d = rut[-1]
            r = list(rut.split('-')[0])
            r = map(int, r)[::-1]
            s = 11 - sum([int(digito) * factor for digito, factor in zip(r, 2 * range(2, 8))]) % 11
            if s == 10:
                s = 'k'
            if s == 11:
                s = 0
            if d == str(s):
                try:
                    usuario = Perfil.objects.get(rut=rut)
                    raise forms.ValidationError('El rut ingresado se encuentra registrado')
                except Perfil.DoesNotExist:
                    pass
            else:
                raise forms.ValidationError('El rut ingresado no es correcto')
        else:
            raise forms.ValidationError('El rut no tiene un formato valido ej: 11111111-1 ó -K')
        return rut


class PerfilFormEdit(forms.ModelForm):

    rut=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Perfil
        exclude = ['usuario']