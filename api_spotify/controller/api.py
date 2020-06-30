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


def get_track(track_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).track(track_id)


def get_artist(artist_id):
    return spotipy.Spotify(auth_manager=get_auth_manager()).artist(artist_id)


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


# Get top tracks in an array
# 0 : Track name
# 1 : Main artist name
# 2 : Album picture url
# 3 : Album url on Spotify
# 4 : Track url on Spotify
# limit = number of items
# time_range = short_term || medium_term || long_term
def get_arr_tracks(limit, time_range):
    results = get_top_tracks(limit, time_range)
    arr_res = [[]]
    for i, item in enumerate(results['items']):
        arr_res[i].append(item['name'])  # Track name
        arr_res[i].append(item['artists'][0]['name'])  # Main artist name
        arr_res[i].append(get_album_pic(item['album']['id']))  # Album picture url
        arr_res[i].append(item['album']['external_urls']['spotify'])  # Album url on spotify
        arr_res[i].append(item['external_urls']['spotify'])  # Track url on Spotify
        arr_res.append([])
    arr_res.pop()
    return arr_res


# Get top artists in an array
# 0 : Artist name
# 1 : Artist picture on spotify
# 2 : Artist id
# 3 : URL to the artist on spotify
# limit = number of items
# time_range = short_term || medium_term || long_term
def get_arr_artists(limit, time_range):
    results = get_top_artist(limit, time_range)
    arr_res = [[]]
    for i, item in enumerate(results['items']):
        arr_res[i].append(item['name'])  # Artist name
        arr_res[i].append(item['images'][0]['url'])  # Artist picture on spotify
        arr_res[i].append(item['id'])  # Artist id
        arr_res[i].append(item['external_urls']['spotify'])  # URL to the artist on spotify
        arr_res.append([])
    arr_res.pop()
    return arr_res


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

print(get_top_tracks(10, "long_term"))
print(get_arr_tracks(10, "short_term"))
