from django.urls import path

from .views import ProfileFormView, ProfileFavoriteListView

urlpatterns = [
    path("profile/", ProfileFormView.as_view(), name="profile"),
    path("profile/favorite/", ProfileFavoriteListView.as_view(), name="favorite"),
]
