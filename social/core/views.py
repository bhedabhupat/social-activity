from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, TemplateView


@login_required
def HomeView(request):
    print(request.user)
    return render(request, 'core/home.html')


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("core:home")