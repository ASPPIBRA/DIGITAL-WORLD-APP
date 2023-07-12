# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - AppSeed.us

New version of the App updated 2023 by - ASPPIBRA-DAO

"""

from django.urls import path, include
from .views import login_view, register_user, delete_account, change_password, RecoveryView , PasswordResetView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete_account/", delete_account, name="delete-account"),
    path("change_password/", change_password, name="change-password"),
    path("recovery_password/", RecoveryView.as_view(), name="recovery-password"),
    path("reset_password/<uidb64>/<token>/", PasswordResetView.as_view(), name="reset-password"),
    path('social_login/', include('allauth.urls')),
]
