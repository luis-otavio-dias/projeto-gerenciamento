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

    def dummy_field(self, web_element, field, text):
        return web_element.find_element(
            By.NAME,
            f"{field}",
        ).send_keys(f"{text}")

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div/div[2]/div/form",
        )

    def form_field_with_callback(self, callback, dummy_data=False):
        self.browser.get(self.live_server_url + "/users/register/")
        form = self.get_form()

        if dummy_data:
            self.fill_form_dummy_data(form)

        callback(form)
        return form

    def test_empty_username_message(self):
        def callback(form):
            username_field = self.get_by_id(form, "id_username")
            username_field.send_keys(" ")
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn("Este campo é obrigatório.", form.text)

        self.form_field_with_callback(callback, dummy_data=True)

    def test_short_password_message(self):
        def callback(form):
            self.dummy_field(form, "username", "user")
            password1 = self.get_by_id(form, "id_password1")
            password2 = self.get_by_id(form, "id_password2")
            password1.send_keys("test")
            password2.send_keys("test")
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn(
                "Esta senha é muito curta."
                " Ela precisa conter pelo menos 8 caracteres.",
                form.text,
            )

        self.form_field_with_callback(callback)

    def test_common_password_message(self):
        def callback(form):
            self.dummy_field(form, "username", "user")
            password1 = self.get_by_id(form, "id_password1")
            password2 = self.get_by_id(form, "id_password2")
            password1.send_keys("12345678")
            password2.send_keys("12345678")
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn(
                "Esta senha é muito comum.",
                form.text,
            )

        self.form_field_with_callback(callback)

    def test_numeric_password_message(self):
        def callback(form):
            self.dummy_field(form, "username", "user")
            password1 = self.get_by_id(form, "id_password1")
            password2 = self.get_by_id(form, "id_password2")
            password1.send_keys("12345678")
            password2.send_keys("12345678")
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn(
                "Esta senha é inteiramente numérica.",
                form.text,
            )

        self.form_field_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            self.dummy_field(form, "username", "user")
            password1 = self.get_by_id(form, "id_password1")
            password2 = self.get_by_id(form, "id_password2")
            password1.send_keys("Password")
            password2.send_keys("Passowrd_Different")
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn(
                "Senhas não coincidem",
                form.text,
            )

        self.form_field_with_callback(callback)
