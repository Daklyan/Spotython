import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .controller import api


def index(request):
    test = ["natane", "autre", "chose"]
    context = {'test': test}
    return HttpResponse(render(request, 'api_spotify/index.html', context))


def detail(request, album_id):
    result = api.test(1, 2)
    message = "AUTRE PAGE {} and result {}".format(album_id, result)
    return HttpResponse(message)


def login(request):
    if request.method == 'GET':
        print("truc")
        api.get_top_artist(10, "short_term")
        return redirect(api.get_auth_manager().get_authorize_url())
    return HttpResponse(request)


def logout(request):
    # response = HttpResponse('/')
    if request.method == 'GET':
        path = os.getcwd() + os.path.sep + '.cache_spotify'
        if os.path.isfile(path):
            os.remove(path)
        # response = logout(request)
        # response.delete_cookie('user_location')
    return request


def logged(request):
    s = api.get_arr_tracks(2, "short_term")
    m = api.get_top_tracks(1, "medium_term")
    l = api.get_top_tracks(1, "long_term")
    result_s = []
    for i in s:
        result_s.append({
            'track_name': i[0],
            'artist_name': i[1],
            'picture_url': i[2],
            'album_url': i[3],
            'track_url': i[4]
        })

    context = {
        'short': result_s,
        'medium': m,
        'long': l
    }
    return HttpResponse(render(request, 'api_spotify/logged.html', context))