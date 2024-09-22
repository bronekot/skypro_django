import random
import string

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic.edit import CreateView, FormView

from .forms import LoginForm, PasswordRecoveryForm, RegisterForm


class PasswordRecoveryView(FormView):
    form_class = PasswordRecoveryForm
    template_name = "password_recovery.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = get_user_model().objects.get(email=email)
        if user:
            new_password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            user.set_password(new_password)
            user.save()
            send_mail(
                "Восстановление пароля",
                f"Ваш новый пароль: {new_password}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            return redirect("users:login")
        return redirect("users:password_recovery")


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
        if user is not None:
            login(self.request, user)
            return redirect("catalog:home")
        return redirect("users:login")


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        try:
            send_mail(
                "Регистрация на сайте",
                "Вы успешно зарегистрировались на сайте!",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
        except Exception as e:
            print(f"Ошибка при отправке письма: {e}")
        login(self.request, user)
        return redirect(reverse_lazy("catalog:home"))


class LogoutView(LogoutView):
    next_page = reverse_lazy("catalog:home")

    def dispatch(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
