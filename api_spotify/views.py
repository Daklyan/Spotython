from django.shortcuts import render
from django.http import HttpResponse
from .controller import api

def index(request):
    test = ["natane", "autre", "chose"]
    context = {'test': test}
    return HttpResponse(render(request, 'api_spotify/index.html', context))

def detail(request, album_id):
    result = api.test(1,2)
    message = "AUTRE PAGE {} and result {}".format(album_id, result)
    return HttpResponse(message)

