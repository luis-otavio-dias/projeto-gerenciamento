from project.students.models import (
    Students,
    Navigators,
    ScheduleAvailability,
    Meeting,
    Task,
    Upload,
)
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.http import Http404


@login_required(login_url="users:login")
def students(request):
    if request.method == "GET":
        navigators = Navigators.objects.filter(owner=request.user)
        students = Students.objects.filter(owner=request.user)

        stages_flat = [i[1] for i in Students.stage_choices]
        qtt_stages = []

        for i, j in Students.stage_choices:
            x = (
                Students.objects.filter(stage=i)
                .filter(
                    owner=request.user,
                )
                .count()
            )
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


@login_required(login_url="users:login")
def register_navigator(request):
    if request.method == "POST":
        name = request.POST.get("nome")
        owner = request.user

        navigator = Navigators(name=name, owner=owner)

        navigator.save()

        messages.add_message(
            request,
            constants.SUCCESS,
            "Mentor cadastrado com sucesso.",
        )

        return redirect("students:student")

    return render(request, "navigator.html")


@login_required(login_url="users:login")
def meeting(request):
    if request.method == "GET":
        meetings = Meeting.objects.filter(date__mentor=request.user)
        return render(request, "meeting.html", {"meetings": meetings})
    else:
        date = request.POST.get("data")
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M")

        availability = ScheduleAvailability.objects.filter(
            initial_date__gte=(date - timedelta(minutes=50)),
            initial_date__lte=(date + timedelta(minutes=50)),
        )

        if availability.exists():
            messages.add_message(
                request,
                constants.ERROR,
                "Você já possui uma reunião em aberto.",
            )
            return redirect("students:meeting")

        availability = ScheduleAvailability(
            initial_date=date,
            mentor=request.user,
        )

        availability.save()
        messages.add_message(
            request,
            constants.SUCCESS,
            "Horário agendado com sucesso.",
        )
        return redirect("students:meeting")


def task(request, id):
    student = Students.objects.get(id=id)

    if student.owner != request.user:
        raise Http404()

    if request.method == "GET":
        tasks = Task.objects.filter(student=student)
        videos = Upload.objects.filter(student=student)

        context = {
            "student": student,
            "tasks": tasks,
            "videos": videos,
        }

        return render(request, "task.html", context)
    else:
        task = Task(
            student=student,
            task=request.POST.get("tarefa"),
        )
        task.save()
        return redirect(f"/students/task/{id}")


def upload(request, id):
    student = Students.objects.get(id=id)

    if student.owner != request.user:
        raise Http404()

    video = request.FILES.get("video")
    upload = Upload(
        student=student,
        video=video,
    )

    upload.save()
    return redirect(f"/students/task/{id}")
