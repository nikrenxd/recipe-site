from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DetailView

from .models import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    slug_url_kwarg = "recipe_slug"
    template_name = "recipes/recipe_detail.html"


class RecipeFavoriteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        slug = self.kwargs.get("meal_slug")
        user = self.request.user

        print(self.kwargs)

        if (pk and slug) and user.is_authenticated:
            recipe = get_object_or_404(Recipe, pk=pk)
            if recipe not in user.favorite_recipes.filter(pk=recipe.pk):
                user.favorite_recipes.add(recipe)
            else:
                user.favorite_recipes.remove(recipe)

        return redirect("meal-recipes", meal_slug=slug)
