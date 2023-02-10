# -*- encoding: utf-8 -*-
"""
ASPPIBRA-DAO
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=((0, 'Female'), (1, 'Male')), default=0)
    phone = models.CharField(max_length=20, default='', blank=True)
    address = models.TextField(default='', blank=True)
    number = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    zipcode = models.CharField(max_length=10, default='', blank=True)
    image = models.URLField(default='')
