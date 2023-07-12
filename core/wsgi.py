# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - AppSeed.us

New version of the App updated 2023 by - ASPPIBRA-DAO

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
