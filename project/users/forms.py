from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    _input_css = "block w-full rounded-md bg-white/5 px-3 py-1.5 text-base\
            text-white outline outline-1 -outline-offset-1 outline-white/10\
            placeholder:text-gray-500 focus:outline focus:outline-2\
            focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"

    username = forms.CharField(
        label="Username",
        required=True,
        min_length=3,
        widget=forms.TextInput(attrs={"class": _input_css}),
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": _input_css}),
        help_text=(
            "Sua senha precisa conter pelo menos 8 caracteres.",
            "Sua senha não pode ser inteiramente numérica.",
        ),
        required=True,
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": _input_css}),
        help_text=("Repita a senha.",),
        required=True,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    "password2",
                    ValidationError("Senhas não coincidem."),
                )

        return super().clean()
