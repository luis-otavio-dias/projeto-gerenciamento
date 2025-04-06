from django.urls import path
from students import views

app_name = "students"

urlpatterns = [
    path("", views.students, name="student"),
    path("meets/", views.meets, name="meets"),
    path("auth/", views.auth_view, name="auth_student"),
    path("select_day/", views.select_day, name="select_day"),
    path("select_day/", views.select_day, name="select_day"),
    path("schedule_meeting/", views.schedule_meeting, name="schedule_meeting"),
]
