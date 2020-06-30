import time
from pathlib import Path

import spotipy
import os
from spotipy import SpotifyOAuth

# Client Id of the application https://developer.spotify.com/dashboard/applications
os.environ['SPOTIPY_CLIENT_ID'] = 'CLIENT ID'
# Client Secret of the application https://developer.spotify.com/dashboard/applications
os.environ['SPOTIPY_CLIENT_SECRET'] = 'CLIENT SECRET'
# URI to redirect after logged in
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8000/logged'
# Cache to store user token
os.environ['CACHE_PATH'] = str((Path(os.getcwd())).parent.parent) + os.path.sep + ".cache_spotify"


def get_username():
    return spotipy.Spotify(auth_manager=get_auth_manager()).current_user()['display_name']


def get_auth_manager():
    scope = 'user-library-read user-top-read'  # Rights given to the app from Spotify
    auth_manager = SpotifyOAuth(os.environ['SPOTIPY_CLIENT_ID'], os.environ['SPOTIPY_CLIENT_SECRET'],
                                os.environ['SPOTIPY_REDIRECT_URI'], scope=scope, cache_path=os.environ['CACHE_PATH'])
    # auth_manager = refresh_token(auth_manager)
    return auth_manager


def refresh_token(auth_manager):
    if auth_manager.get_cached_token()['expires_at'] < time.time():
        auth_manager.refresh_access_token()
        return auth_manager
    return auth_manager


# Get the top artist of the user
# Limit = limit number of tracks
# Time range = short_term || medium_term || long_term
def get_top_artist(limit, time_range):
    return spotipy.Spotify(auth_manager=get_auth_manager()).current_user_top_artists(time_range=time_range, limit=limit)


# Get the top tracks of the user
# Limit = limit number of tracks
# Time range = short_term || medium_term || long_term
def get_top_tracks(limit, time_range):
    return spotipy.Spotify(auth_manager=get_auth_manager()).current_user_top_tracks(time_range=time_range, limit=limit)


# Get the track from his id
def get_track(track_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).track(track_id)


# Search the artist from his id
def get_artist(artist_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).artist(artist_id)


# Get albums from an artist id
def get_artist_albums(artist_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).artist_albums(artist_id)


def get_album(album_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).album(album_id)


def get_album_pic(album_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).album(album_id)['images'][0]['url']


# Search a track, an artist, an album,...
# search_string : what to search for
# limit = Limit number of items to get
def search_smth(search_string, limit):
    return spotipy.Spotify(auth_manager=get_auth_manager()).search(q=search_string, limit=limit)


# ============================= DEBUG =======================================

def display_top_tracks(limit, time_range):
    results = get_top_tracks(limit, time_range)
    for i, item in enumerate(results['items']):
        print('#', i + 1, '.', item['name'], '-', item['artists'][0]['name'])


def display_top_artist(limit, time_range):
    results = get_top_artist(limit, time_range)
    for i, item in enumerate(results['items']):
        print('#', i + 1, '.', item['name'])


#  ========================== TEST FIELD ====================================
#
# print(get_auth_manager().get_cached_token())
# display_top_artist(10, 'long_term')
# print(get_top_artist(10, 'short_term'))
# print(search_smth("american idiot", 5))
# print(search_smth("Judas Priest", 10))
# print(get_artist('2tRsMl4eGxwoNabM08Dm4I')['name'])
# print(search_smth('Ipséité', 10))
# print(get_album_pic('7JJ1Zqwc0m0cDyXXodXCqb'))
# print(get_artist_albums('2tRsMl4eGxwoNabM08Dm4I'))
#
# print(get_top_artist(10, 'short_term'))
# print(get_auth_manager().get_cached_token())
# refresh_token(get_auth_manager())
# print(get_auth_manager().get_cached_token())

