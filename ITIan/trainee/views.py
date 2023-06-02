from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from course.models import *
def traineelist(request):
    if( 'username' in request.session):
        trainees=trainee.objects.all()
        context={}
        context['trainees']=trainees
        return  render(request,'trainee/list.html',context)#HttpResponse('hi from trainee list view')
    else:
        return HttpResponseRedirect('/')

# def traineeadd(req):
#     return  render(req,'trainee/add.html')
# def traineeupdate(req,id):
#     return HttpResponseRedirect('/trainees')

# def traineeDelete(request,ID):
#     return  HttpResponse('hi id ='+str(ID)+' deleted')




def traineelist(request):
    if( 'username' in request.session):
        trainees=trainee.objects.all()
        context={}
        context['trainees']=trainees
        return  render(request,'trainee/list.html',context)#HttpResponse('hi from trainee list view')
    else:
        return HttpResponseRedirect('/')

def traineeadd(req):
    if ('username' in req.session):
        context={}
        context['courses']=Course.objects.all()
        if(req.method=='POST'):
            cou=Course.objects.filter(id=req.POST['course'])
            trainee.objects.create(trainee_name=req.POST['trainee_name'],email=req.POST['email'],course_id=cou[0])
        return  render(req,'trainee/add.html',context) #HttpResponse('hi from add trainee view')
    else:
        return  HttpResponseRedirect('/')
def traineeupdate(req,ID):
    context={}
    context['courses']=Course.objects.all
    data=trainee.objects.filter(trainee_id=ID)[0]
    context['traineedata']=data
    if(req.method=='POST'):
        trainee.objects.filter(trainee_id=ID).update(trainee_name=req.POST['trainee_name'],course_id=Course.objects.get(id=req.POST['course']) )
        return HttpResponseRedirect('/trainee/list')

    return render(req,'trainee/update.html',context)

def traineeDelete(request,ID):
    #delete from trainee-trainee where id=ID
    trainee.objects.filter(trainee_id=ID).delete()
    return  HttpResponseRedirect('/trainee/list')#HttpResponse('hi id ='+str(ID)+' deleted')