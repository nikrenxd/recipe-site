from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .forms import ProfileEditForm


CustomUser = get_user_model()


class ProfileFormView(LoginRequiredMixin, FormView):
    form_class = ProfileEditForm
    success_url = reverse_lazy("profile")
    template_name = "users/profile_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user

        kwargs["instance"] = user

        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileFavoriteListView(LoginRequiredMixin, ListView):
    template_name = "users/favorite_list.html"
    context_object_name = "favorites"

    def get_queryset(self):
        user = self.request.user
        qs = user.favorite_recipes.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = self.get_queryset().count()
        return context
