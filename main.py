import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CID")
SECRET = os.getenv("SPOTIFY_SECRET")
USER_NAME = os.getenv("USER_NAME")
AUTH_ENDPOINT = "https://accounts.spotify.com/authorize?"
SCOPE = "playlist-modify-private"
# auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENT_ID,
    client_secret=SECRET,
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.user(USER_NAME)["id"]
print(user_id)

# params = {
#     "response_type": "code",
#     "client_id": CLIENT_ID,
#     "scope": SCOPE,
#     "redirect_uri": "http://example.com",
#     "state": "asdjkqitowktleof",
# }

# response = requests.get(url=AUTH_ENDPOINT, params=params)
# response.raise_for_status
# print(response.text)

# user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}")
# response.raise_for_status
# content = response.text

# soup = BeautifulSoup(content, "html.parser")

# song_title_list = soup.select("div ul li ul h3")
# song_title_names = [song.text.strip() for song in song_title_list]
# song_uris = []

# year = user_date.split("-")[0]
# for song in song_title_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     # print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped")

# playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} BIllboard 100", public=False)
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
