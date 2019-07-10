# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class homee(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    #contact_no = models.IntegerField(null=True)
    #slug = models.SlugField(unique=True, null=True)
    password = models.CharField(max_length=100)
    #address = models.ForeignKey('address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.id)


class address(models.Model):
    city = models.CharField(max_length=30)
    service_area = models.CharField(max_length=100)
    local_address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=120, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return str(self.user)
