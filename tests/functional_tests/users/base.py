from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser


class UserBaseFunctionalTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def make_user(
        self,
        username="user",
        password1="teste1234",
    ):
        return User.objects.create_user(
            username=username,
            password=password1,
        )
