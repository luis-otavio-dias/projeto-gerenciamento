from users.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    user = RegisterForm()

    if request.method == "POST":
        user = RegisterForm(request.POST)

        if user.is_valid():
            user.save()
            messages.add_message(request, constants.SUCCESS)
            return redirect("users:login")

    return render(request, "users/register.html", {"user": user})


def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect("/students/")
        messages.add_message(
            request,
            constants.ERROR,
            "Username ou senha inválidos.",
        )
        return redirect("users:login")


@login_required(login_url="users:login")
def logout_view(request):
    auth.logout(request)
    return redirect("users:login")
