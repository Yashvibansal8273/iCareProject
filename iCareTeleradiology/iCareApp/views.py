from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from .models import CustomUser
from django.http import HttpResponse
def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

    
def study_list(request):
    return render(request, 'study_list.html')


def contact_us(request):
    return render(request, 'contact_us.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from .models import CustomUser

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("signup successfully")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username_or_phone = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate by username or phone number
            user = authenticate(request, username=username_or_phone, password=password)
            if not user:
                user = CustomUser.objects.filter(phone_number=username_or_phone).first()
                if user and user.check_password(password):
                    login(request, user)
                    return redirect('dashboard')  # Redirect to dashboard after login
                else:
                    messages.error(request, "Invalid credentials")
            else:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = LoginForm()

    return render(request, 'home.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')  # Render the dashboard template