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
    #return HttpResponse(request)


def logout(request):
    if request.method == 'GET':
        path = os.getcwd() + os.path.sep + 'api_spotify' + os.path.sep + 'controller' + os.path.sep + '.cache_spotify'
        if os.path.isfile(path):
            os.remove(path)
    return HttpResponse(request)


def logged(request):
    print(request)
    test = ["natane", "autre", "chose", "tru"]
    print("test avant")
    test_api = api.get_top_tracks(1, "short_term")
    print(test_api)
    # print("test")
    context = {'test': test_api}
    return HttpResponse(render(request, 'api_spotify/index.html', context))