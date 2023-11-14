from django.views import View
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from comments.forms import CommentForm


class RecipeDetailView(DetailView):
    model = Recipe
    slug_url_kwarg = "recipe_slug"
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Recipe
    slug_url_kwarg = "recipe_slug"
    template_name = "recipes/recipe_detail.html"

    def form_valid(self, form):
        recipe = self.get_object()
        form.instance.user = self.request.user
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        self.object = self.get_object()
        return self.object.get_absolute_url()


class RecipeView(View):
    def get(self, request, *args, **kwargs):
        view = RecipeDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreateView.as_view()
        return view(request, *args, **kwargs)
