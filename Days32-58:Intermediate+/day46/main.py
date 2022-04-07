from urllib import response
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import sys
import pprint

spotify_ID = "1e389a7d0b4e45d9817f9ad8ac5b7602"
spotify_key = "804524a49822473cab0a86203bceaafc"
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=spotify_ID, client_secret=spotify_key, redirect_uri="http://example.com", scope="playlist-modify-private", show_dialog=True,cache_path="Days32-58:Intermediate+/day46/token.txt"))

user_id = sp.current_user()["id"]

# year = "2021-09-14"
# YYYY = "2021"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")
top100_web_page = response.text

soup = BeautifulSoup(top100_web_page, "html.parser")

all_songs = soup.select("div ul li ul li h3")
songs_list = [" ".join(song.getText().split()) for song in all_songs]
song_uris = []
i = 0
year = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD" )
YYYY = year.split("-")[0]

with open("Days32-58:Intermediate+/day46/songs.txt", "w") as file:
	for song in songs_list:
		i += 1
		if i == 101:
			break
		file.write(song)
		file.write('\n')

		search_str = f"track:{song} year:{YYYY}"
		result = sp.search(q=search_str, type="track")
		# pprint.pprint(result)

		try:
			uri = result["tracks"]["items"][0]["uri"]
			song_uris.append(uri)
		except IndexError:
			print(f"{song} doesn't exist in Spotify. Skipped.")
   
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

