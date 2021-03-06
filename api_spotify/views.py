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
    if 'login' in request.session:
        del request.session['login']
    # # response = HttpResponse('/')
    # if request.method == 'GET':
    #     path = os.getcwd() + os.path.sep + '.cache_spotify'
    #     if os.path.isfile(path):
    #         os.remove(path)
    #     # response = logout(request)
    #     # response.delete_cookie('user_location')
    # return request
    return HttpResponse(render(request, 'api_spotify/index.html'))


def logged(request):
    request.session['login'] = True
    s = api.get_arr_tracks(50, "short_term")
    m = api.get_arr_tracks(50, "medium_term")
    l = api.get_arr_tracks(50, "long_term")
    result_s = []
    result_m = []
    result_l = []
    for j, i in enumerate(s):
        result_s.append({
            'track_name': i[0],
            'artist_name': i[1],
            'picture_url': i[2],
            'album_url': i[3],
            'track_url': i[4],
            'album_name': i[5],
            'artist_url': i[6],
            'iter': '#' + str(j + 1) + " - "
        })

    for j, i in enumerate(m):
        result_m.append({
            'track_name': i[0],
            'artist_name': i[1],
            'picture_url': i[2],
            'album_url': i[3],
            'track_url': i[4],
            'album_name': i[5],
            'artist_url': i[6],
            'iter': '#' + str(j + 1) + " - "
        })

    for j, i in enumerate(l):
        result_l.append({
            'track_name': i[0],
            'artist_name': i[1],
            'picture_url': i[2],
            'album_url': i[3],
            'track_url': i[4],
            'album_name': i[5],
            'artist_url': i[6],
            'iter': '#' + str(j + 1) + " - "
        })

    context = {
        'short': result_s,
        'medium': result_m,
        'long': result_l
    }
    return HttpResponse(render(request, 'api_spotify/logged.html', context))

def artiste(request):
    s = api.get_arr_artists(50, "short_term")
    m = api.get_arr_artists(50, "medium_term")
    l = api.get_arr_artists(50, "long_term")
    result_s = [({
            'artiste_name': i[0],
            'artiste_picture': i[1],
            'artiste_id': i[2],
            'artist_url': i[3],
            'iter': '#' + str(j + 1) + " - "
        }) for j, i in enumerate(s)]

    result_m = [({
            'artiste_name': i[0],
            'artiste_picture': i[1],
            'artiste_id': i[2],
            'artist_url': i[3],
            'iter': '#' + str(j + 1) + " - "
        }) for j, i in enumerate(m)]

    result_l = [({
            'artiste_name': i[0],
            'artiste_picture': i[1],
            'artiste_id': i[2],
            'artist_url': i[3],
            'iter': '#' + str(j + 1) + " - "
        }) for j, i in enumerate(l)]


    context = {
        'short': result_s,
        'medium': result_m,
        'long': result_l
    }
    return HttpResponse(render(request, 'api_spotify/artiste.html', context))