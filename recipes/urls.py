from django.urls import path

from .views import RecipeDetailView

urlpatterns = [
    path(
        "<slug:meal_slug>/<slug:recipe_slug>/",
        RecipeDetailView.as_view(),
        name="recipe-detail",
    ),
]
