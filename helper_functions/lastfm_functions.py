import json
from typing import List, Optional, Tuple
import requests
from constants import LASTFM_API_KEY


def get_artists_lastfm(artist: str) -> Optional[Tuple[List[str], str]]:
    url_name = f"http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={artist}&api_key={LASTFM_API_KEY}&format=json&limit=1"
    url_similar_artists = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key={LASTFM_API_KEY}&format=json&limit=20"
    artist_json = requests.get(url_name)
    artist_name = ""
    if artist_json.status_code != 200:
        print("Error retrieving artist from Last.fm")
    else:
        artist_name = artist_json.json()["results"]["artistmatches"]["artist"][0][
            "name"
        ]

    related_artists_json = requests.get(url_similar_artists)
    if related_artists_json.status_code != 200:
        print("Error retrieving related artists from Last.fm")
    else:
        return (
            list(
                map(
                    lambda artist: artist["name"],
                    related_artists_json.json()["similarartists"]["artist"],
                )
            ),
            artist_name,
        )
