import pytest

from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from .base import UserBaseFunctionalTest
from django.urls import reverse


@pytest.mark.functional_test
class UserLoginTest(UserBaseFunctionalTest):
    def test_user_can_login_successfully(self):
        user = self.make_user()
        self.browser.get(self.live_server_url + reverse("users:login"))

        form = self.browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div[2]/div/form",
        )

        username = self.get_input_by_name(form, "username")
        password = self.get_input_by_name(form, "senha")
        username.send_keys(user.username)
        password.send_keys(user.password)

        form.submit()
