import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
import os
load_dotenv()


def get_saved_tracks():
    """
    Fetches all the saved tracks for the user ( this is the liked songs in spotify )
    :param client_id: client_id for the app [ found in the api dashboard ]
    :param secret_key: secret_key for the app [ found in the api dashboard ]
    :param redirectURI: redirect URI for authentication
    <!-------------Need to setup params for this function----------------!>

    """
    #load creadentials
    SPOTIPY_CLIENT_ID  = os.getenv('ClientId')
    SPOTIPY_REDIRECT_URI = os.getenv('RedirectURI')
    SPOTIPY_CLIENT_SECRET = os.getenv('SecretKey')

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI,scope=scope))



    results = sp.current_user_saved_tracks(limit=50, offset=50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'],"-", track['name'])
    
    """
    TO-DO:
    - run a loop to get all the saved tracks for the user, for now we can only get 50 tracks in one request
    - store all the tracks in a list and share that as an output for this function
    """


def get_devices():
    pass

def get_user_info():
    pass

def get_user_playlists():
    pass

def get_tracks_from_playlists():
    pass
