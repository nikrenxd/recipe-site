from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm


CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("email", "name", "is_active", "is_staff")
    search_fields = ("email", "name")
    ordering = ["email"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("name",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
