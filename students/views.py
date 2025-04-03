from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from students.models import Students, Navigators


# Create your views here.
def students(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "GET":
        navigators = Navigators.objects.filter(owner=request.user)
        students = Students.objects.filter(owner=request.user)
        return render(
            request,
            "students.html",
            {
                "stages": Students.stage_choices,
                "navigators": navigators,
                "students": students,
            },
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
