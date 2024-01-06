
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from myapp.forms import *
from django.contrib.auth.models import User
# Create your views here.


@login_required
def admin(request):
    emploi=job.objects.all()
    context={
        'emploi':emploi,
    }
    return render(request,"admin/admin.html",context)

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def createjob(request):
    if request.method=='POST':
        form=jobform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin") 
        return render(request,'admin/createjob.html',{'form':form})
    else :
     form= jobform
     return render(request,'admin/createjob.html',{'form':form})
    
@login_required
def updatejob(request,pk):
    stag=job.objects.get(id=pk)
    form=jobform(instance=stag)
    if request.method=='POST':
        form=jobform(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("admin") 
    return render(request,'admin/updatejob.html',{'form':form})


def deletejob(request,pk):
    item=job.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("admin") 
    return render(request,'admin/deletejob.html',{'item':item})