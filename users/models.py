from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from recipes.models import Recipe


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=155, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    favorite_recipes = models.ManyToManyField(Recipe, blank=True)

    username = None
    first_name = None
    last_name = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
