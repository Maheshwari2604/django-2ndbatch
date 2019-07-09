# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    try:
        print('hello')
        return HttpResponse('hey wass up')
    except:
        print('error')

def view(request):
    print('heyyyyy')
    return HttpResponse('lkjhgfdsa')