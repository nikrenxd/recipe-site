from django.views.generic import DetailView

from .models import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    slug_url_kwarg = "recipe_slug"
    template_name = "recipes/recipe_detail.html"
