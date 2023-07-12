# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - AppSeed.us

New version of the App updated 2023 by - ASPPIBRA-DAO

"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static

urlpatterns = []

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.accounts.urls")),
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
]

