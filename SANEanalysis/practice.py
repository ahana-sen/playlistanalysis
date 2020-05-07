import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = "74d2b05f4e4c490daaa4b7d1fb0a2177"
client_secret = "865dd84e8dc04935a6d181dbf764889b"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

pl_id = 'spotify:playlist:0ThF3wyjhsWQPItf2s7M3V'


response = sp.playlist_tracks(pl_id)


exdf = {}
exdf["adderID"] = []
exdf['danceability'] = []
exdf['energy'] = []
exdf['loudness'] = []
exdf['speechiness'] = []
exdf['instrumentalness'] = []
exdf['tempo'] =[]
exdf['duration_ms'] = []
exdf['songname'] = []
exdf['artistname'] = []
exdf['popularity'] = []
exdf['genre'] = []
exdf['releasedate'] = []



for item in response['items']:
    exdf["adderID"].append(item['added_by']['id'])
    tempfeat = sp.audio_features(item['track']['uri'])
    exdf["danceability"].append(tempfeat[0]['danceability'])
    exdf["energy"].append(tempfeat[0]['energy'])
    exdf["loudness"].append(tempfeat[0]['loudness'])
    exdf["speechiness"].append(tempfeat[0]['speechiness'])
    exdf["instrumentalness"].append(tempfeat[0]['instrumentalness'])
    exdf["tempo"].append(tempfeat[0]['tempo'])
    exdf["duration_ms"].append(tempfeat[0]['duration_ms'])
    name = item['track']['artists'][0]['name']
    exdf["artistname"].append(name)
    song = item['track']['name']
    exdf["songname"].append(song)
    popu = item['track']['popularity']
    exdf["popularity"].append(popu)
    reldate = item['track']['album']['release_date']
    exdf['releasedate'].append(reldate)
    genres = sp.artist(item['track']['artists'][0]['uri'])
    genrel = genres["genres"]
    exdf['genre'].append(genrel)

acdf = pd.DataFrame.from_dict(exdf)

acdf.to_csv("test.csv")
