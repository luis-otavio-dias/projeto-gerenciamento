from django.urls import path
from students import views

app_name = "students"

urlpatterns = [
    path("", views.students, name="student"),
    path("meets/", views.meets, name="meets"),
]
