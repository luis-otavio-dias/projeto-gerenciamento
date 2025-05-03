from project.users.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        username = request.POST.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(
                request,
                constants.ERROR,
                "Username já cadastrado.",
            )
            return redirect("users:register")

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                constants.SUCCESS,
                "Registro realizado com sucesso.",
            )
            return redirect("users:login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


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
