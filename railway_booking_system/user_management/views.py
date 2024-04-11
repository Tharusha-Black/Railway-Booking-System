from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from .forms import SignupForm, LoginForm

class IndexView(View):
    def get(self, request):
        return render(request, 'user_management/index.html')

class UserSignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'user_management/sign_up.html', {'form': form})
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'user_management/sign_up.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user_management/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard') if user.is_superuser else redirect('search_trains')
        return render(request, 'user_management/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
