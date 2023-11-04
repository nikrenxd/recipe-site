from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .services import (
    create_token_and_send_email,
    token_verification,
    token_expired,
    get_timestamp_difference,
)
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
        create_token_and_send_email(self.request, form)
        return super().form_valid(form)


class ConfirmEmailView(TemplateView):
    template_name = "confirmation/confirm_success_page.html"

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=kwargs["id"])
        token = kwargs["token"]
        expired_minutes = get_timestamp_difference(token)

        if token_expired(user, expired_minutes):
            return redirect("expired")

        if not token_verification(self.request, user, token):
            return redirect("used")

        return super().get(request, *args, **kwargs)


class ExpiredEmailView(TemplateView):
    template_name = "confirmation/token_expired.html"


class UsedTokenView(TemplateView):
    template_name = "confirmation/token_used.html"
