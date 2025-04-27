import pytest
from .base import HomePageBaseFunctionalTest
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class HomePageTest(HomePageBaseFunctionalTest):
    def test_click_mentor_login(self):
        self.browser.get(self.live_server_url)
        links = self.browser.find_elements(By.XPATH, "//div/a")
        links[1].click()

    def test_click_aluno_auth(self):
        self.browser.get(self.live_server_url)
        links = self.browser.find_elements(By.XPATH, "//div/a")
        links[2].click()
