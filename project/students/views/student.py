from project.students.models import (
    Students,
    ScheduleAvailability,
    Meeting,
    Task,
    Upload,
)
from project.students.auth import validate_token
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.conf import settings
from django.http import Http404, HttpResponse
import locale


locale.setlocale(locale.LC_TIME, settings.LANGUAGE_CODE.replace("-", "_"))


def auth_view(request):
    if request.method == "GET":
        return render(request, "auth_student.html")
    elif request.method == "POST":
        token = request.POST.get("token")

        if not Students.objects.filter(token=token).exists():
            messages.add_message(request, constants.ERROR, "Token inválido.")
            return redirect("students:auth_student")

        response = redirect("students:select_day")
        response.set_cookie("auth_token", token, max_age=3600)

        return response


def select_day(request):
    if not validate_token(request.COOKIES.get("auth_token")):
        return redirect("auth_student")

    if request.method == "GET":
        student = validate_token(request.COOKIES.get("auth_token"))

        availabilities = ScheduleAvailability.objects.filter(
            initial_date__gte=datetime.now(),
            scheduled=False,
            mentor=student.owner,
        ).values_list("initial_date", flat=True)

        dates, months, days = [], [], []

        for i in availabilities:
            dates.append(i.date().strftime("%d-%m-%Y"))
            months.append(i.date().strftime("%B").capitalize())
            days.append(i.date().strftime("%A").capitalize())

        context = {
            "schedules": list(set(dates)),
            "months": list(set(months)),
            "days": list(set(days)),
        }
        return render(request, "select_day.html", context)


def schedule_meeting(request):
    if not validate_token(request.COOKIES.get("auth_token")):
        return redirect("students:auth_student")

    student = validate_token(request.COOKIES.get("auth_token"))

    if request.method == "GET":
        date = request.GET.get("date")
        date = datetime.strptime(date, "%d-%m-%Y")

        schedules = ScheduleAvailability.objects.filter(
            initial_date__gte=date,
            initial_date__lt=date + timedelta(days=1),
            scheduled=False,
            mentor=student.owner,
        )

        context = {
            "schedules": schedules,
            "tags": Meeting.tag_choices,
        }

        return render(request, "schedule_meeting.html", context)

    else:
        schedule_id = request.POST.get("horario")
        tag = request.POST.get("tag")
        description = request.POST.get("descricao")

        if ScheduleAvailability.objects.filter(id=schedule_id).exists():
            meeting = Meeting(
                date_id=schedule_id,
                student=student,
                tag=tag,
                description=description,
            )
            meeting.save()

            schedule = ScheduleAvailability.objects.get(id=schedule_id)
            schedule.scheduled = True
            schedule.save()

            messages.add_message(
                request,
                constants.SUCCESS,
                "Reunião agendada com sucesso.",
            )

            return redirect("students:select_day")
        else:
            messages.add_message(
                request,
                constants.ERROR,
                "Horário não encontrado.",
            )
            return redirect("students:select_day")


def student_task(request):
    student = validate_token(request.COOKIES.get("auth_token"))
    if not student:
        return redirect("students:auth_student")

    if request.method == "GET":
        videos = Upload.objects.filter(student=student)
        tasks = Task.objects.filter(student=student)
        context = {
            "student": student,
            "videos": videos,
            "tasks": tasks,
        }

        return render(request, "student_task.html", context)


@csrf_exempt
def toggle_task(request, id):
    student = validate_token(request.COOKIES.get("auth_token"))
    if not student:
        return redirect("students:auth_student")

    task = Task.objects.get(id=id)
    if student != task.student:
        raise Http404()
    task.executed = not task.executed
    task.save()
    return HttpResponse("teste")
