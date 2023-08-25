
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm 


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url = reverse_lazy('login'))

def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html', {"error": "Пользователя нет, ёмаё"})

def register_view(request): 
    if request.POST == 'POST': 
        form = CustomUserCreationForm() 
        if form.is_valid(): 
            form.save() 
    else: 
        form = CustomUserCreationForm() 
    context = { 
        'form':form 
    } 
    return render(request, 'app_auth/register.html', context) 

