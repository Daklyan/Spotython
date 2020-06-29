import spotipy
import traceback
from spotipy import SpotifyOAuth
import spotipy.util as util
import os
import webbrowser

os.environ['SPOTIPY_CLIENT_ID'] = 'CLIENT ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'CLIENT SECRET'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8000/logged'


def get_auth_manager():
    scope = 'user-library-read user-top-read'
    auth_manager = SpotifyOAuth(os.environ['SPOTIPY_CLIENT_ID'], os.environ['SPOTIPY_CLIENT_SECRET'],
                                os.environ['SPOTIPY_REDIRECT_URI'], scope=scope)
    return auth_manager


def connection(auth_manager):
    webbrowser.open(auth_manager.get_authorize_url(), new=0)


print(get_auth_manager().get_authorize_url())

