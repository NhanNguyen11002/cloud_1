# from django.shortcuts import render
from django.http import JsonResponse, Http404
from . import GameControl

def game_server(request, tiles):
    
    if request.method == 'POST':
        if 'gid' not in request.POST.keys():
            # Game Creation
            if 'init' not in request.POST.keys():
                raise Http404("Bad Request!")
            return JsonResponse(GameControl.create_game(tiles))
        else:
            # Getting Game State
            gameobj = GameControl.ret_game(request.POST['gid'])
            if not gameobj:
                raise Http404("Bad Request")
            if 'move[]' in request.POST.keys():
                if not GameControl.move(request.POST['gid'], request.POST.getlist('move[]')):
                    raise Http404("Bad Request")
            return JsonResponse(gameobj)
    else:
        raise Http404("Bad Request!")
