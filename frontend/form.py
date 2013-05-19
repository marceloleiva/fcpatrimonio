# -*- coding: utf-8 -*-
__author__ = 'Marcelo'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(help_text="", widget=forms.TextInput(
        attrs={'placeholder': 'Correo electronico',
               'class': 'login username-field',
               'required': 'required'}
    ))
    password = forms.CharField(help_text=" ", widget=forms.PasswordInput(render_value=False,
        attrs={'placeholder': 'Contraseña',
            'class': 'login password-field',
            'required': 'required'}
    ))
