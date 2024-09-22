from django import forms

from .models import CustomUser


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "avatar", "phone_number", "country")


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField(label="Email")
