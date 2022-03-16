import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '1e9ed5dc714d4ddb845be0be6921c767'
secret = '429e7f402e654ec28e6a73500db8c47e'
id_artist = '6vWDO969PvNqNYHIOW5v0m'
name_artist = ""
popularity = ""
followers = 0
genres = []

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist(id_artist)

name_artist = results.get('name', 'not encountered')
popularity = results.get('popularity')
followers = results.get('followers')
total = followers.get('total')
genres = results.get('genres')


print(f'Nome: {name_artist} \n'
      f'Popularity: {popularity}\n'
      f'Followers: {total}\n'
      f'Genres: {genres[0]}, {genres[1]},{genres[2]}')