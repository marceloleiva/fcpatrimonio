# -*- coding: utf-8 -*-
__author__ = 'Marcelo'

from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(help_text="", widget=forms.TextInput(
        attrs={'placeholder': 'Correo electrónico',
               'class': 'login username-field',
               'required': 'required',}
    ))
    password = forms.CharField(help_text=" ", widget=forms.PasswordInput(render_value=False,
        attrs={'placeholder': 'Contraseña',
            'class': 'login password-field',
            'required': 'required'}
    ))
