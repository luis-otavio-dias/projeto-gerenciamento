from django.urls import path
from project.home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
]
