# import django
from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser

# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


# django.setup()


class HomePageBaseFunctionalTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
