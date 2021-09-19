from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




# Create your views here.
def homeview(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)

def registeruser(request):
    form=RegisterUser()
    if request.method =='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def loginuser(request):
    if request.method =='POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user')
    template_name='login.html'
    return render(request,template_name)

def logoutuser(request):
    logout(request)
    return redirect('register')

def change_password(request):
    form=PasswordChangeForm(request.user)
    if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        
    
    template_name='change_password.html'
    context={'form':form}
    return render(request,template_name,context)



