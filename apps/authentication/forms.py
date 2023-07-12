# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - AppSeed.us

New version of the App updated 2023 by - ASPPIBRA-DAO

"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from apps.authentication.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de usuário",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de usuário",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Verificação de senha",
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class RecoveryForm(forms.Form):
    email = forms.EmailField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model().objects.filter(email=email)

        if not user.exists():
            raise ValidationError('Não há nenhum usuário com este e-mail')
        return email