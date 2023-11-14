from django.urls import path

from .views import MealsListView, MealRecipesListView, RecipeFavoriteView


urlpatterns = [
    path("meals-list/", MealsListView.as_view(), name="meals-list"),
    path(
        "meals-list/<slug:meal_slug>/",
        MealRecipesListView.as_view(),
        name="meal-recipes",
    ),
    path(
        "add-to-favorite/<slug:meal_slug>/<slug:recipe_slug>/<int:pk>/",
        RecipeFavoriteView.as_view(),
        name="recipe-favorite",
    ),
]
