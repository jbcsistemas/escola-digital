from django import forms
from django.contrib.auth.forms import AuthenticationForm


class FormEntrar(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingUsuario',
                'placeholder': 'Nome de Usuário',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingSenha',
                'placeholder': 'Senha',
            }
        )
    )
