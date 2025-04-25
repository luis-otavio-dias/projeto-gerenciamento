# import time
import django
from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser

# from django.core.management import call_command

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


django.setup()


# from selenium.webdriver.support.wait import WebDriverWait


class HomePageTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_the_test(self):
        browser = self.browser
        browser.get(self.live_server_url)
        browser.quit()
