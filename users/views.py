from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "users/register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")
        confirm_password = request.POST.get("confirmar_senha")

        if password != confirm_password:
            messages.add_message(
                request,
                constants.ERROR,
                "Senha e confirmar senha devem ser iguais.",
            )
            return redirect("users:register")

        if len(password) < 6:
            messages.add_message(
                request,
                constants.ERROR,
                "Senha deve ter no mínimo 6 dígitos.",
            )
            return redirect("users:register")

        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(
                request,
                constants.ERROR,
                "Username já cadastrado.",
            )
            return redirect("users:register")

        User.objects.create_user(
            username=username,
            password=password,
        )

        return redirect("users:login")


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
            return redirect("/mentorados/")
        messages.add_message(
            request,
            constants.ERROR,
            "Username ou senha inválidos.",
        )
        return redirect("users:login")
