from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
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
        password="P@ssw0rd",
    ):
        return User.objects.create_user(
            username=username,
            password=password,
        )

    def get_input_by_id(self, web_element, id):
        return web_element.find_element(By.XPATH, f"//input[@id='{id}']")

    def get_input_by_name(self, web_element, name):
        return web_element.find_element(By.XPATH, f"//input[@name='{name}']")
