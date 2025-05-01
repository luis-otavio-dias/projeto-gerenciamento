from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserLogoutTest(TestCase):
    def test_user_tries_to_logout(self):
        User.objects.create_user(username="user", password="password")
        self.client.login(username="user", password="password")

        response = self.client.post(
            reverse("users:logout"),
            follow=True,
        )

        self.assertRedirects(
            response,
            "/users/login/",
        )
