import base64
from typing import Dict, List, Optional, Tuple
import requests
from constants import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def get_token() -> Optional[str]:
    url = "https://accounts.spotify.com/api/token"
    b64_credentials = base64.b64encode(
        f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()
    ).decode("utf-8")
    body = {
        "grant_type": "client_credentials",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_credentials}",
    }
    response = requests.post(url, data=body, headers=headers)
    if response.status_code != 200:
        print("Error retrieving token from Spotify")
    else:
        return response.json()["access_token"]


def get_artist_id_spotify(artist: str, token: str) -> Optional[Tuple[str, str]]:
    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error retrieving artist id from Spotify")
    else:
        return (
            response.json()["artists"]["items"][0]["id"],
            response.json()["artists"]["items"][0]["name"],
        )


def get_artist_spotify(artist: str) -> Optional[Tuple[List[str], str]]:
    token = get_token()
    if token is None:
        print("No token Spotify")
        return
    data = get_artist_id_spotify(artist, token)
    if data is None:
        print("No artist found on Spotify")
        return
    artist_id, artist_name = data
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = {"Authorization": f"Bearer {token}"}
    related_artists = requests.get(url, headers=headers)
    if related_artists.status_code != 200:
        print("Error retrieving related artists from Spotify")
    else:
        return (
            list(map(lambda artist: artist["name"], related_artists.json()["artists"])),
            artist_name,
        )
