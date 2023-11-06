from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Meal


class MealsListView(ListView):
    model = Meal
    template_name = "meals/meals_list.html"
    context_object_name = "meals"


class MealRecipesListView(ListView):
    template_name = "meals/meal_recipes.html"
    context_object_name = "meal_recipes"

    def get_queryset(self):
        meal_slug = self.kwargs.get("meal_slug")
        meal = get_object_or_404(Meal, slug=meal_slug)
        qs = meal.recipe_set.filter(meal__slug=meal_slug)
        return qs
