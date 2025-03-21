from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib import messages


# Function to login User
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            next_url = request.GET.get('next', '/')
            login(request, user)
            return HttpResponse('Hello World')
        else:
            messages.error(request, "Invalid PEN or Password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return HttpResponse('Hello World')