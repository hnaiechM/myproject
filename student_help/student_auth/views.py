from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                auth_login(request, user)  # Use auth_login to avoid conflict
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed!')
                return render(request, 'login.html', {'form': form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = User.objects.create_user(username=username, password=pwd)
            if user is not None:
                return redirect("login")
            else:
                messages.error(request, 'Account creation failed!')
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
