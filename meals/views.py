from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View


from recipes.models import Recipe
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meal_slug"] = self.kwargs["meal_slug"]
        return context


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


class RecipeFavoriteView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HTTPResponseHXRedirect(redirect_to=reverse("login"))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        slug = self.kwargs.get("slug")
        user = request.user

        context = {}
        if pk:
            recipe = get_object_or_404(Recipe, pk=pk)
            context["recipe"] = recipe
            context["meal_slug"] = slug
            if recipe not in user.favorite_recipes.filter(pk=recipe.pk):
                user.favorite_recipes.add(recipe)
                return render(request, "meals/partials/remove.html", context)
            user.favorite_recipes.remove(recipe)
            return render(request, "meals/partials/add.html", context)
