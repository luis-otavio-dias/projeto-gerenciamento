from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class RegisterForm(UserCreationForm):
    _input_css = "block w-full rounded-md bg-white/5 px-3 py-1.5 text-base\
            text-white outline outline-1 -outline-offset-1 outline-white/10\
            placeholder:text-gray-500 focus:outline focus:outline-2\
            focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"

    username = forms.CharField(
        required=True,
        min_length=3,
        widget=forms.TextInput(attrs={"class": _input_css}),
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": _input_css}),
        help_text=password_validation.password_validators_help_text_html(),
        required=True,
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        strip=False,
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": _input_css}),
        help_text="Repita a senha.",
        required=True,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data(self.username)

        if User.objects.filter(username=username).exists():
            self.add_error(
                "username",
                ValidationError("Username já cadastrado.", code="invalid"),
            )

        return username

    def clean(self):
        password1 = self.cleaned_data.get("senha")
        password2 = self.cleaned_data.get("confirmar_senha")

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    "confirmar_senha", ValidationError("Senhas não coincidem.")
                )

        return super().clean()
