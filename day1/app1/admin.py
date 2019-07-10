# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import homee , address
from django.contrib import admin

# Register your models here.
class homeee(admin.ModelAdmin):
    list_display = ['firstname' , 'lastname' , 'email']
    list_editable = ['email']
    search_fields = ['email']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated']

    class meta:
        model = homee

admin.site.register(homee, homeee)


admin.site.register(address)



#KNCBDAJCVAG.COM/shivam-maheshwari
    