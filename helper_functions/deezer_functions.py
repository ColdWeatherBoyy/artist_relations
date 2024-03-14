from typing import List, Optional, Tuple
import requests


def get_artists_deezer(artist: str) -> Optional[Tuple[List[str], str]]:
    artist_json = requests.get(
        f"https://api.deezer.com/search/artist?q={artist}&limit=20"
    )
    if artist_json.status_code != 200:
        print("Error retrieving artist from Deezer")
    else:
        artist_id = artist_json.json()["data"][0]["id"]
        artist_name = artist_json.json()["data"][0]["name"]
        related_artists_json = requests.get(
            f"https://api.deezer.com/artist/{artist_id}/related"
        )
        if (
            related_artists_json.status_code != 200
            or related_artists_json.json()["data"] == []
        ):
            print("Error retrieving related artists from Deezer")
        else:
            return (
                list(
                    map(
                        lambda artist: artist["name"],
                        related_artists_json.json()["data"],
                    )
                ),
                artist_name,
            )
