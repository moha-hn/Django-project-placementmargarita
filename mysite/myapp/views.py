
from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib import messages
from .forms import *

from django.views.generic import CreateView
from django.contrib.auth import login,authenticate

from .models import *
from django.contrib.auth.models import User

from .filters import *
from .forms import *

from gestion.urls import *


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .filters import *
from django.core.mail import EmailMessage

from django.template.loader import render_to_string
#main website

def indexesp(request):
    return render(request,"main/indexesp.html")

def indexfr(request):
    return render(request,"main/indexfr.html")





def contactesp(request):
    return render(request,"main/contactesp.html")

def emploifr(request):
    emploi=job.objects.all()
    myfilter=jobfilter(request.GET ,queryset=emploi)
    emploi=myfilter.qs
    context={
        'emploi':emploi,
        'myfilter':myfilter
    }
    return render(request,"main/emploifr.html",context)

def emploiesp(request):
    emploi=job.objects.all()
    myfilter=jobfilteresp(request.GET ,queryset=emploi)
    emploi=myfilter.qs
    context={
        'emploi':emploi,
        'myfilter':myfilter
    }
    return render(request,"main/emploiesp.html",context)


#login
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if  user is not None :
                    login(request, user)
                    return redirect('admin')
    return render(request,'login-cover.html',context={'form':AuthenticationForm()})




def contactfr(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = request.POST.get('name')
            msg = request.POST.get('message')
            mail = request.POST.get('email')
            message = render_to_string("email/emailcontact.html",{
            'message':msg,
            'email':mail,
            'nom':subject,
            })
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["placementmargaritainc@gmail.com"]    
            send_mail( subject, message, from_email , recipient_list ,fail_silently=True)  
            return redirect('contactfr')
    else:
        form = ContactForm()

    return render(request, 'main/contactfr.html', {'form': form})

def contactesp(request):
    if request.method == 'POST':
        form = ContactFormesp(request.POST)
        if form.is_valid():
            form.save()
            subject = request.POST.get('name')
            msg = request.POST.get('message')
            mail = request.POST.get('email')
            message = render_to_string("email/emailcontact.html",{
            'message':msg,
            'email':mail,
            'nom':subject,
            })
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["placementmargaritainc@gmail.com"]    
            send_mail( subject, message, from_email , recipient_list ,fail_silently=True)  
            return redirect('contactfr')
    else:
        form = ContactFormesp()

    return render(request, 'main/contactesp.html', {'form': form})





def formesp(request):
    if request.method == 'POST':
        form = candidatformesp(request.POST)
        if form.is_valid():
            form.save()
            jobb=request.POST.get('job')
            subject = job.objects.get(id=jobb)
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            mail = request.POST.get('email')
            body = render_to_string("email/emailcandidat.html",{
            'nom':nom,
            'prenom':prenom,
            'email':mail,
            'job':subject,
            })
            from_email = settings.EMAIL_HOST_USER
            uploaded_file = request.FILES['cv'] 
            email = EmailMessage(
                subject,
                body,
                from_email,
                ["placementmargaritaemployes@gmail.com",],
            )
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.send(fail_silently=True)

            return redirect('emploiesp')
    else:
        form = candidatformesp()

    return render(request, 'main/formesp.html', {'form': form})


    

def formfr(request):
    
    if request.method == 'POST':
        form = candidatform(request.POST)
        if form.is_valid():
            form.save()
            jobb=request.POST.get('job')
            subject = job.objects.get(id=jobb)
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            mail = request.POST.get('email')
            body = render_to_string("email/emailcandidat.html",{
            'nom':nom,
            'prenom':prenom,
            'email':mail,
            'job':subject,
            })
            from_email = settings.EMAIL_HOST_USER
            email = EmailMessage(
                subject,
                body,
                from_email,
                ["placementmargaritaemployes@gmail.com",],
                
            )
            if request.FILES:      
                uploaded_file = request.FILES['cv'] 
                email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.send(fail_silently=True)

            return redirect('emploifr')
    else:
        form = candidatform()

    return render(request, 'main/formfr.html', {'form': form})
