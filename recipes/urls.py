from django.urls import path

from .views import RecipeDetailView

urlpatterns = [
    path("<slug:recipe_slug>/", RecipeDetailView.as_view(), name="recipe-detail"),
]
