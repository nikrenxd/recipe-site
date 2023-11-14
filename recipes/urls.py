from django.urls import path

from .views import RecipeView

urlpatterns = [
    path(
        "<slug:meal_slug>/<slug:recipe_slug>/",
        RecipeView.as_view(),
        name="recipe-detail",
    ),
]
