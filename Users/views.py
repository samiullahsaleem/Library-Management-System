from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="/users/loginform/", redirect_field_name="next")
def profile(request):
    User = models.User.objects.get(username=request.user)
    return render(request, "Users/profile.html", {"user": request.user, "User": User})

@login_required(login_url="/users/loginform/", redirect_field_name="next")
def logoutform(request):
    logout(request)
    return redirect("loginform")

def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            newUser = models.User(username=user["username"], password=user["password"], email=user["email"], fullname=user["fullname"])
            newUser.save()
            user = User.objects.create_user(username=user["username"], password=user["password"])
            user.save()
            return render(request, "Users/login.html", {"form": form, "success": True})
    else:
        form = forms.UserRegisterForm()
    return render(request, "Users/register.html",{ "form": form})

def loginform(request):
    if request.method == "POST":
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                return render(request, "Users/login.html", {"form": form, "error": True})
    else:
        form = forms.UserLoginForm()
        return render(request, "Users/login.html", {"form": form})

