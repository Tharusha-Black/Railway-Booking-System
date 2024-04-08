from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# Home page
def index(request):
    return render(request, 'user_management/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'user_management/sign_up.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            if user.is_superuser:
                return redirect('dashboard')  # Redirect superusers to dashboard
            else:
                return redirect('search_trains')  # Redirect regular users to home
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('home')
