import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import UserBaseFunctionalTest


@pytest.mark.functional_test
class UserResgisterTest(UserBaseFunctionalTest):
    def get_by_id(self, web_element, id):
        return web_element.find_element(By.XPATH, f"//input[@id='{id}']")

    def fill_form_dummy_data(self, web_element):
        fields = web_element.find_elements(By.TAG_NAME, "input")

        for field in fields:
            if field.is_displayed():
                field.send_keys(" " * 20)

    def test_empty_username_message(self):
        self.browser.get(self.live_server_url + "/users/register/")
        form = self.browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div[2]/div/form",
        )

        self.fill_form_dummy_data(form)

        username_field = self.get_by_id(form, "id_username")
        username_field.send_keys(" ")
        username_field.send_keys(Keys.ENTER)

        form = self.browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div[2]/div/form",
        )

        self.assertIn("Este campo é obrigatório.", form.text)
