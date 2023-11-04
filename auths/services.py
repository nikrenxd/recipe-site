from django.core.mail import send_mail
from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.http import base36_to_int
from django.contrib.auth.tokens import default_token_generator


def create_token_and_send_email(request, form):
    token = default_token_generator.make_token(form.instance)
    activation_link = request.build_absolute_uri(
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


def get_timestamp_difference(token):
    timestamp = base36_to_int(token.split("-")[0])
    timestamp_minutes = datetime.fromtimestamp(timestamp).minute
    now_time_minutes = datetime.now().minute

    return now_time_minutes - timestamp_minutes


def token_expired(user, expired_minutes):
    if expired_minutes > 3:
        if user is not None and not user.is_active:
            print("Work")
            user.delete()
            # return redirect("expired")
        return True


def token_verification(request, user, token):
    token_used = request.session.get("token_used", False)

    if default_token_generator.check_token(user, token) and not token_used:
        if not user.is_active:
            request.session["token_used"] = True

            del request.session["token_used"]
            user.is_active = True
            user.save()
            return True
        return False
