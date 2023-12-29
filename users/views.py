from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, ("Usuario ou senha incorretos!"))
            return redirect("login_user")
    else:
        return render(request, 'users/login.html', {})

@login_required(login_url='login_user')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html')
    else:
        return render(request, 'users/login.html')
    
@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')