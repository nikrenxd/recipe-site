from django.contrib import admin

from .models import Meal
from recipes.models import Recipe


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("type",)}
    search_fields = ["type"]
    inlines = [RecipeInline]
