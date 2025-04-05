from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from students.models import Students, Navigators


# Create your views here.
@login_required(login_url="users:login")
def students(request):
    if request.method == "GET":
        navigators = Navigators.objects.filter(owner=request.user)
        students = Students.objects.filter(owner=request.user)

        stages_flat = [i[1] for i in Students.stage_choices]
        qtt_stages = []

        for i, j in Students.stage_choices:
            x = Students.objects.filter(stage=i).filter(owner=request.user).count()
            qtt_stages.append(x)

        context = {
            "stages": Students.stage_choices,
            "navigators": navigators,
            "students": students,
            "stages_flat": stages_flat,
            "qtt_stages": qtt_stages,
        }

        return render(
            request,
            "students.html",
            context,
        )

    elif request.method == "POST":
        name = request.POST.get("nome")
        picture = request.FILES.get("foto")
        stage = request.POST.get("estagio")
        navigator = request.POST.get("navigator")

        student = Students(
            name=name,
            picture=picture,
            stage=stage,
            navigator_id=navigator,
            owner=request.user,
        )

        student.save()

        messages.add_message(
            request,
            constants.SUCCESS,
            "Mentorado cadastrado com sucesso.",
        )
        return redirect("students:student")


def meets(request):
    if request.method == "GET":
        return render(request, "meets.html")
    elif request.method == "POST":
        ...
