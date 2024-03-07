from typing import List, Optional
import requests


def get_artists_deezer(artist: str) -> Optional[List[str]]:
    json = requests.get(f"https://api.deezer.com/search/artist?q={artist}")
    if json.status_code == 200:
        artist_id = json.json()["data"][0]["id"]
        related_artists = requests.get(
            f"https://api.deezer.com/artist/{artist_id}/related"
        )
        if related_artists.status_code == 200:
            return list(
                map(lambda artist: artist["name"], related_artists.json()["data"])
            )
    else:
        print("Error retrieving related artists from Deezer")
