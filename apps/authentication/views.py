# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - AppSeed.us

New version of the App updated 2023 by - ASPPIBRA-DAO

"""

# Create your views here.
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from core.settings import GITHUB_AUTH, TWITTER_AUTH
from .forms import LoginForm, SignUpForm, RecoveryForm
from apps import Utils
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credenciais inválidas'
        else:
            msg = 'Erro ao validar o formulário'

    return render(request, "accounts/login.html", {"form": form, "msg": msg,
                                                    "github_login": GITHUB_AUTH, "twitter_login": TWITTER_AUTH})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuário criado com sucesso.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'O formulário não é válido'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def delete_account(request, **kwargs):
    result, message = Utils.delete_user(request.user.username)
    if not result:
        return JsonResponse({
            'errors': message
        }, status=400)
    logout(request)
    return HttpResponseRedirect('/')


def change_password(request, **kwargs):
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        message = 'Password successfully changed.'
        status = 200
    else:
        message = form.errors
        status = 400
    return JsonResponse({
        'message': message
    }, status=status)

class RecoveryView(SuccessMessageMixin, FormView):
    template_name = 'accounts/forgot_password.html'
    form_class = RecoveryForm
    success_url = reverse_lazy('recovery-password')
    success_message = 'Solicitação realizada com sucesso!'
    extra_context = {
        'title': 'Recuperação de senha',
    }

    def form_valid(self, form):
        email = self.request.POST.get("email")
        user = get_user_model().objects.get(email=email)
        context = {
					"email":user.email,
					'domain':settings.DOMAIN,
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': settings.ACCOUNT_DEFAULT_HTTP_PROTOCOL,
                    }
        subject = 'Solicitação de redefinição de senha'
        html_content = render_to_string('accounts/emails/recovery_email.html', context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return super().form_valid(form)

class PasswordResetView(
    SuccessMessageMixin, auth_views.PasswordResetConfirmView
):
    template_name = 'accounts/reset_password.html'
    success_url = reverse_lazy('login')
    success_message = ('Password reset complete')
