from django.shortcuts import render, redirect

# Create your views here.
from game_app.games.forms import GameCreateForm, GameEditForm, GameDeleteForm
from game_app.games.models import GameModel


def game_create(request):
    form = GameCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard games')

    context = {
        'form': form
    }
    return render(request, 'games/create-game.html', context=context)


def game_edit(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game details', pk)
    context = {
        'form': form
    }
    return render(request, 'games/edit-game.html', context=context)


def game_delete(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard games')

    form = GameDeleteForm(initial=game.__dict__)

    context = {
        'form': form
    }
    return render(request, 'games/delete-game.html', context=context)


def game_details(request, pk):
    game = GameModel.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'games/details-game.html', context=context)
