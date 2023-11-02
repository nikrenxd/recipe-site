from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView, ConfirmEmailView, ExpiredEmailView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "activate/<int:id>/<str:token>/",
        ConfirmEmailView.as_view(),
        name="activate",
    ),
    path("activate/expired/", ExpiredEmailView.as_view(), name="expired"),
]
