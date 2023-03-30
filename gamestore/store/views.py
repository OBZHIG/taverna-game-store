from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'store/signup.html'

def home(request):
    games = Game.objects.all()
    return render(request, 'store/home.html', {'games': games})


def sale(request):
    games = Game.objects.filter(is_on_sale=True)
    return render(request, 'store/sale.html', {'games': games})


def game(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'store/game.html', {'game': game})