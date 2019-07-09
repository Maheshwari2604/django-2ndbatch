# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class homee(models.Model):
    firstname = models.CharField(max_length=250, help_text='Required')
    lastname = models.CharField(max_length=250, help_text='Required')
    username = models.CharField(max_length=250, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    #contact_no = models.IntegerField(null=True)
    #slug = models.SlugField(unique=True, null=True)
    password = models.CharField(max_length=100)
    #address = models.ForeignKey('address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
