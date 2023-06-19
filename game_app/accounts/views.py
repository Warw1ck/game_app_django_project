from django.shortcuts import render, redirect
from game_app.accounts.forms import CreateProfileForm, EditProfileForm
from game_app.accounts.models import ProfileModel
from game_app.games.models import GameModel


def profile_create(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'accounts/create-profile.html', context=context)


def profile_edit(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk)
    context = {
        'form': form
    }
    return render(request, 'accounts/edit-profile.html', context=context)


def profile_delete(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    return render(request, 'accounts/delete-profile.html')


def profile_details(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    games = GameModel.objects.all()

    context = {
        'profile': profile,
        'number_games': len(games),
        'average_rating': sum([game.rating for game in games])/len(games)
    }
    return render(request, 'accounts/details-profile.html', context=context)
