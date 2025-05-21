from django.urls import path
from project.students import views

app_name = "students"

urlpatterns = [
    path("", views.students, name="student"),
    # Navigator/User
    path("navigator/", views.register_navigator, name="navigator"),
    path("meeting/", views.meeting, name="meeting"),
    path("task/<int:id>", views.task, name="task"),
    path("upload/<int:id>", views.upload, name="upload"),
    # Student
    path("auth/", views.auth_view, name="auth_student"),
    path("select_day/", views.select_day, name="select_day"),
    path("schedule_meeting/", views.schedule_meeting, name="schedule_meeting"),
    path("student_task/", views.student_task, name="student_task"),
    path("toggle_task/<int:id>", views.toggle_task, name="toggle_task"),
    # API
    path("api/", views.students_list, name="students_list"),
    path("api/<int:pk>/", views.student_detail, name="student_detail"),
    path("api/task/", views.task_list, name="task_list"),
    path("api/task/<int:pk>/", views.task_detail, name="task_detail"),
]
