# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import homee
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    try:
        print('hello')
        a = homee.objects.all()
        print(a)
        for i in a:
            print(i.email)

        #print(i.email)
        #return HttpResponse('hey wass up')
        context = {
            'message': 'hey wass up',
            'name': 'hey shivam',
            'p': a
        }
        
    except:
        context = {
            'message': 'error',
            'name': 'hey none'
        }
        print('error')

    return render(request , 'app1/aa.html' , context=context)
        

def view(request , id):
    print('heyyyyy')
    #i = homee.objects.get(id = id)
    return render(request , 'app1/bb.html')

def cc(request):
    print('heyyyyy')
    return render(request , 'app1/cc.html')
       