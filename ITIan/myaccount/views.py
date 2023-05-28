from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Login(req):
    return render(req,'login.html')

def Logout():

    return HttpResponse('Logout')

def Registration(req):

    context={}
    context['title']='To Do List'
    context['user']='normal'
    return  render(req,'register.html',context)