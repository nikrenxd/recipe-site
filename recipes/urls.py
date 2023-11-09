from django.urls import path

from .views import RecipeDetailView, RecipeFavoriteView

urlpatterns = [
    path(
        "<slug:meal_slug>/<slug:recipe_slug>/",
        RecipeDetailView.as_view(),
        name="recipe-detail",
    ),
    path(
        "add-to-favorite/<slug:meal_slug>/<slug:recipe_slug>/<int:pk>/",
        RecipeFavoriteView.as_view(),
        name="recipe-favorite",
    ),
]
