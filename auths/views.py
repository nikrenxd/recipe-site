from django.views.generic import FormView
from django.urls import reverse_lazy

from users.forms import CustomUserCreationForm


class SignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
