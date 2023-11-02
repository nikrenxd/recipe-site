from datetime import datetime, timedelta
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils.http import base36_to_int
from django.contrib.auth.tokens import default_token_generator

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class SignupView(FormView):
    form_class = CustomUserCreationForm
    model = CustomUser
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.is_active = False
        form.save()
        token = default_token_generator.make_token(form.instance)
        activation_link = self.request.build_absolute_uri(
            reverse_lazy(
                "activate",
                kwargs={
                    "id": form.instance.id,
                    "token": token,
                },
            )
        )
        send_mail(
            "Account activation",
            f"Here is your link\n{activation_link}",
            "admin@mail.com",
            [form.instance.email],
        )

        return super().form_valid(form)


class ConfirmEmailView(TemplateView):
    template_name = "confirmation/confirm_success_page.html"

    def get(self, request, *args, **kwargs):
        token = kwargs["token"]
        user_id = kwargs["id"]
        user = None

        timestamp = base36_to_int(token.split("-")[0])
        timestamp_minutes = datetime.fromtimestamp(timestamp).minute
        now_time = datetime.now().minute

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return redirect("home")

        if (now_time - timestamp_minutes) < 5 and user is not None:
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
        else:
            user.delete()
            return redirect("expired")

        return super().get(request, *args, **kwargs)


class ExpiredEmailView(TemplateView):
    template_name = "confirmation/token_expired.html"
