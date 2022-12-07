from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic


def game(request, tiles):

    # Checking if no. of tiles is very high or low
    if tiles > 20 or tiles < 3:
        return HttpResponseBadRequest("<h1>No of tiles is not in bound [3,20]!")

    return render(request, 'game/game.html', {
        'tiles': tiles,
        'tiles_range': range(tiles),
    })
