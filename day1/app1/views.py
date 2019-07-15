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
        
        
    #     print "in try"
    # #csrfContext = RequestContext(request)
    #     print ("hey")
        
    #     else:
    #         print "no_post but error"
    #         del request.session['user_id']
    #         del request.session['cart_id'] 
    
        
    except:
        context = {
            'message': 'error',
            'name': 'hey none'
        }
        print('error')

    return render(request , 'app1/aa.html' , context=context)
        

def view(request):


    #<a href='{% url 'khbgjj' product.id %}'></a>
    print('heyyyyy')
    if request.method == 'POST':
        u = homee()
        email = request.POST['email']
        print(email)
        u.firstname = request.POST['firstname']
        u.lastname = request.POST['lastname']
        u.email = request.POST['email']
        #u.firstname = 'll'
        u.save()
        uu = request.session['email']
        print('session is: ')
        print(uu)



        if request.session['email']:





    else:
        print('error')
    #ixx = homee.objects.get(id = id)
    return render(request , 'app1/bb.html')

def cc(request):
    print('heyyyyy')
    return render(request , 'app1/cc.html')
       











    # if request.method == 'POST':
    #         print "register in post"
    #         user = homee()
    #         username = request.POST['first_name']
    #         print(username)
    #         user.save()
    # else:
    #     print('error')  