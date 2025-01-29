import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
import os
load_dotenv()


def get_saved_tracks(client_id, secret_key, redirect_uri):
    """
    Fetches all the saved tracks for the user ( this is the liked songs in spotify )
    :param client_id: client_id for the app [ found in the api dashboard ]
    :param secret_key: secret_key for the app [ found in the api dashboard ]
    :param redirectURI: redirect URI for authentication
    """

    #defines permissions required for the request call
    scope = "user-library-read"

    #authenticate user for request call
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=secret_key,redirect_uri=redirect_uri,scope=scope))

    counter = 0
    while sp.current_user_saved_tracks(offset=counter):
        results = sp.current_user_saved_tracks(limit=50, offset=counter)
        if len(results['items']) != 0:
            for idx, item in enumerate(results['items']):
                track = item['track']
                print(idx, track['artists'][0]['name'],"-", track['name'])
            counter += 50 
        else:
            break
    
    #code to store all the tracks in a list
    tracks = []

    return tracks
    
    """
    TO-DO:
    - store all the tracks in a list and share that as an output for this function
    """


def get_devices():
    #do we need this? 
    pass

def get_user_info(client_id, secret_key, redirect_uri):

    """
    Fetches the user information for the current user 
    :param client_id: client_id for the app [ found in the api dashboard ]
    :param secret_key: secret_key for the app [ found in the api dashboard ]
    :param redirectURI: redirect URI for authentication
    """


    #defines permissions required for the request call
    scope = "user-library-read"

    #authenticate user for the request
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=secret_key,redirect_uri=redirect_uri,scope=scope))
    user_info = sp.current_user()

    print(json.dumps(user_info))

    return user_info

def get_user_playlists(client_id, secret_key, redirect_uri):
    
    """
    Fetches all playlists for the current user 
    :param client_id: client_id for the app [ found in the api dashboard ]
    :param secret_key: secret_key for the app [ found in the api dashboard ]
    :param redirectURI: redirect URI for authentication
    """

    #defines permissions required for the request call
    scope = "user-library-read"

    #authenticate user for the request
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=secret_key,redirect_uri=redirect_uri,scope=scope))
    
    results = sp.current_user_playlists(limit=50)
    playlists = []
    for idx, item in enumerate(results['items']):
        playlist_name = item['name']
        playlists.append(playlist_name)
        print(idx, playlist_name)

    return playlists



def get_tracks_from_playlists():
    pass



if __name__ == "__main__":

    load_dotenv()

    client_id = os.getenv('ClientID')
    secret_key = os.getenv('SecretKey')
    redirect_uri = os.getenv('RedirectURI')

    get_saved_tracks(client_id,secret_key,redirect_uri)

    print('below is the user info for the current user: \n \n')
    get_user_info(client_id,secret_key,redirect_uri)


    print('below are the playlists of the current user: \n \n')
    get_user_playlists(client_id,secret_key,redirect_uri)
