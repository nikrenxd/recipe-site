from django.db import models
from django.utils.text import slugify

from users.models import CustomUser


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    recipe_image = models.ImageField(upload_to="static/images/recipes/")
    slug = models.SlugField()

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    stand_time = models.PositiveIntegerField()
    total_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=220)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe.title}: {self.ingredient}"


class Instruction(models.Model):
    step = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe.title}: {self.step[:100]}"
