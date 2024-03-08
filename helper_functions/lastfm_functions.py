from typing import List, Optional
import requests
from constants import LASTFM_API_KEY


def get_artists_lastfm(artist: str) -> Optional[List[str]]:
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key={LASTFM_API_KEY}&format=json&limit=20"
    related_artists = requests.get(url)
    if related_artists.status_code != 200:
        print("Error retrieving related artists from Last.fm")
    else:
        return list(
            map(
                lambda artist: artist["name"],
                related_artists.json()["similarartists"]["artist"],
            )
        )
