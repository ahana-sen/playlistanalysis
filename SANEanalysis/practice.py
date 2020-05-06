import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

client_id = "74d2b05f4e4c490daaa4b7d1fb0a2177"
client_secret = "865dd84e8dc04935a6d181dbf764889b"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

pl_id = 'spotify:playlist:0ThF3wyjhsWQPItf2s7M3V'
offset = 0

while True:
    response = sp.playlist_tracks(pl_id,
                                  offset=offset,
                                  fields='items.track.id,total')
    pprint(response['items'])
    if len(response['items']) == 0:
        break
        x=2