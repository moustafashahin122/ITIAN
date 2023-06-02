from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from .models import *


def userlist(request):
    context={}
    for u in MyUser.objects.all():
        print(u.id,u.username)
    context['users']=MyUser.objects.all()
    return  render(request,'listusers.html',context)

def Login(req):
    context={}
    if(req.method=='POST'):
        #xquery([obj1])
        u=MyUser.objects.filter(username=req.POST['email'],password=req.POST['password'])
        print(u[0].username)
     
        if(len(u)!=0):
            #add username in session
            req.session['username']=u[0].username
            return HttpResponseRedirect('/trainee')
        else:
            context['msg']='invalid email or password'
    return render(req,'login.html',context=context)

def Logout(req):
    req.session.clear()
    return HttpResponse('Logout')

def Registration(req):
   context={}
   if(req.method =='POST'):
       username=req.POST['username']
       password=req.POST['password']
       email=req.POST['email']
       MyUser.objects.create(username=username,password=password,email=email,active=1)

   return  render(req,'register.html',context)