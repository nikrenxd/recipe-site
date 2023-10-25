from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


CustomUser = get_user_model()


class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
