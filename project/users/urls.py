from django.urls import path
from project.users import views

app_name = "users"

urlpatterns = [
    path("", views.register, name="register"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # API urls
    path("api/", views.user_api_list, name="user_api_list"),
]
