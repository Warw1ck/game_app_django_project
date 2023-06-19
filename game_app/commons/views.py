from django.shortcuts import render

# Create your views here.
from game_app.accounts.models import ProfileModel
from game_app.games.models import GameModel


def home_page(request):
    profile = ProfileModel.objects.all()
    context = {

        'profile': profile
    }
    return render(request, 'commons/home-page.html', context=context)


def dashboard_page(request):
    games = GameModel.objects.all()

    context = {
        'games': games,

    }
    return render(request, 'commons/dashboard.html', context=context)

