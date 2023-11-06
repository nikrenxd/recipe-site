from django.urls import path

from .views import MealsListView, MealRecipesListView


urlpatterns = [
    path("meals-list/", MealsListView.as_view(), name="meals-list"),
    path(
        "meals-list/<slug:meal_slug>/",
        MealRecipesListView.as_view(),
        name="meal-recipes",
    ),
]
