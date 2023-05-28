from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def traineelist(request):
    trainees=[(1,'trainee1'),(2,'trainee2'),(3,'trainee3')]
    context={}
    context['trainees']=trainees
    return  render(request,'trainee/list.html',context)
    # return HttpResponse("hello")

def traineeadd(req):
    return  render(req,'trainee/add.html') 
def traineeupdate(req,id):
    return HttpResponseRedirect('/trainees') 

def traineeDelete(request,ID):
    return  HttpResponse('hi id ='+str(ID)+' deleted')