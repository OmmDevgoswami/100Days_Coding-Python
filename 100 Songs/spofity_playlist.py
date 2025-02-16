import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import os
from dotenv import load_dotenv
from song_tracker import Songlist

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SCERET")
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))
user_id = sp.current_user()["id"]

dateVal = input("Enter the data you want the songs of(in yyyy-mm-dd format): ")
playlist_name = f"100 Top Songs on {dateVal}"
playlist_description = "Created using Python and Spotipy"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
print(f"Playlist '{playlist_name}' created successfully!")

track_uris = []

songs = Songlist(dateVal)
song_dict = songs.finalList()
for song, artist in song_dict.items():
    query = f"{song} {artist}"
    result = sp.search(q=query, limit=1, type="track")
    
    if result["tracks"]["items"]:
        track_uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(track_uri)
        print(f"✅ Found: {song} - {artist} → {track_uri}")
    else:
        print(f"❌ Not Found: {song} - {artist}")

playlist_name = "My Python Playlist"
playlist_description = "Created with Python and Spotipy"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

print(f"🎵 Playlist '{playlist_name}' created successfully!")

if track_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
    print("🎶 Songs added to the playlist!")
else:
    print("⚠️ No valid songs found to add.")