# -*- encoding: utf-8 -*-
"""
ASPPIBRA-DAO
"""

from django.urls import path, include
from .views import login_view, register_user, delete_account, change_password
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete_account/", delete_account, name="delete-account"),
    path("change_password/", change_password, name="change-password"),
    path('social_login/', include('allauth.urls')),
]
