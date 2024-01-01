import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv()

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Set up Spotify client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Now you can use the `sp` object to interact with the Spotify API











# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_client_id",
                                               client_secret="your_client_secret",
                                               redirect_uri="your_redirect_uri",
                                               scope="user-modify-playback-state"))

def play_song(song_uri, device_id=None):
    if device_id:
        sp.start_playback(device_id=device_id, uris=[song_uri])
    else:
        sp.start_playback(uris=[song_uri])

# Correct URI for "Here with Me" by d4vd
song_uri = 'spotify:track:5LrN7yUQAzvthd4QujgPFr'

# Play song on active device
play_song(song_uri)

# Optionally, to play on a specific device:
# devices = sp.devices()
# device_id = next((device['id'] for device in devices['devices'] if device['is_active']), None)
# play_song(song_uri, device_id)
