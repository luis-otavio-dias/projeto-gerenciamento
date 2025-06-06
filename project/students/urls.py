from django.urls import path
from project.students import views

app_name = "students"

urlpatterns = [
    path("", views.students, name="student"),
    path("meeting/", views.meeting, name="meeting"),
    path("auth/", views.auth_view, name="auth_student"),
    path("select_day/", views.select_day, name="select_day"),
    path("schedule_meeting/", views.schedule_meeting, name="schedule_meeting"),
    path("task/<int:id>", views.task, name="task"),
    path("upload/<int:id>", views.upload, name="upload"),
    path("student_task/", views.student_task, name="student_task"),
    path("toggle_task/<int:id>", views.toggle_task, name="toggle_task"),
    path("navigator", views.navigator_view, name="navigator"),
]
