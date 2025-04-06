from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from students.models import Students, Navigators, ScheduleAvailability, Meeting
from datetime import datetime, timedelta
from students.auth import validate_token
from django.conf import settings
import calendar
import locale

locale.setlocale(locale.LC_TIME, settings.LANGUAGE_CODE.replace("-", "_"))


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


@login_required(login_url="users:login")
def meets(request):
    if request.method == "GET":
        return render(request, "meets.html")
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
            return redirect("students:meets")

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
        return redirect("students:meets")


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

    if request.method == "GET":
        date = request.GET.get("date")
        date = datetime.strptime(date, "%d-%m-%Y")

        student = validate_token(request.COOKIES.get("auth_token"))

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
        schedule_id = request.POST.get("schedule_id")
        tag = request.POST.get("tag")
        description = request.POST.get("description")

        meeting = Meeting(
            date_id=schedule_id,
            student=validate_token(request.COOKIES.get("auth_token")),
            tag=tag,
            description=description,
        )
