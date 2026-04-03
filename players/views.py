from django.shortcuts import render, redirect, get_object_or_404
from .models import VolleyPlayer
from .forms import VolleyPlayerForm


def index(request):
    """Home page – list all players (READ)."""
    players = VolleyPlayer.objects.all().order_by('player_id')
    return render(request, 'players/player_list.html', {'players': players})


def add_player(request):
    """CREATE a new player."""
    if request.method == 'POST':
        form = VolleyPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = VolleyPlayerForm()
    return render(request, 'players/player_form.html', {'form': form, 'action': 'Add'})


def view_player(request, pk):
    """READ a single player's details."""
    player = get_object_or_404(VolleyPlayer, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})


def edit_player(request, pk):
    """UPDATE an existing player."""
    player = get_object_or_404(VolleyPlayer, pk=pk)
    if request.method == 'POST':
        form = VolleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = VolleyPlayerForm(instance=player)
    return render(request, 'players/player_form.html', {'form': form, 'action': 'Edit'})


def delete_player(request, pk):
    """DELETE a player."""
    player = get_object_or_404(VolleyPlayer, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'players/player_confirm_delete.html', {'player': player})
