import spotipy
import os
from spotipy import SpotifyOAuth

# Client Id of the application https://developer.spotify.com/dashboard/applications
os.environ['SPOTIPY_CLIENT_ID'] = 'bc588e09eb5e4b3a8e01068e211953e9'
# Client Secret of the application https://developer.spotify.com/dashboard/applications
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b87f5f087a95447e8f502058096b476d'
# URI to redirect after logged in
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8000/logged'
# Cache to store user token
os.environ['cache_path'] = '.cache_spotify'


def get_auth_manager():
    scope = 'user-library-read user-top-read'  # Rights given to the app from Spotify
    token = SpotifyOAuth(os.environ['SPOTIPY_CLIENT_ID'], os.environ['SPOTIPY_CLIENT_SECRET'],
                         os.environ['SPOTIPY_REDIRECT_URI'], scope=scope, cache_path=os.environ['cache_path'])
    return token


# Get the top artist of the user
# Limit = limit number of tracks
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


# Search a track, an artist, an album,...
# search_string : what to search for
# limit = Limit number of items to get
def search_smth(search_string, limit):
    return spotipy.Spotify(auth_manager=get_auth_manager()).search(q=search_string, limit=limit)
