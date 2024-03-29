import base64
import json
from typing import List, Optional, Tuple
import requests
from constants import TIDAL_CLIENT_ID, TIDAL_CLIENT_SECRET


def get_token() -> Optional[str]:
    url = "https://auth.tidal.com/v1/oauth2/token"
    b64_credentials = base64.b64encode(
        f"{TIDAL_CLIENT_ID}:{TIDAL_CLIENT_SECRET}".encode()
    ).decode("utf-8")
    body = {
        "grant_type": "client_credentials",
    }
    headers = {
        "Authorization": f"Basic {b64_credentials}",
    }
    response = requests.post(url, data=body, headers=headers)
    if response.status_code != 200:
        print("Error retrieving token")
    else:
        return response.json()["access_token"]


def get_artist_id_tidal(artist: str, token: str) -> Optional[Tuple[str, str]]:
    url = f"https://openapi.tidal.com/search?query={artist}&type=ARTISTS&limit=10&countryCode=US"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/vnd.tidal.v1+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 207:
        print("Error retrieving artist id from Tidal")
    else:
        return (
            response.json()["artists"][0]["id"],
            response.json()["artists"][0]["resource"]["name"],
        )


def get_related_artists_ids_tidal(artist_id: str, token: str) -> Optional[List[str]]:

    url = (
        f"https://openapi.tidal.com/artists/{artist_id}/similar?countryCode=US&limit=20"
    )
    headers = {
        "Authorization ": f"Bearer {token}",
        "Content-Type": "application/vnd.tidal.v1+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error retrieving related artists' ids from Tidal")
    else:
        return list(
            map(
                lambda artist: artist["resource"]["id"],
                response.json()["data"],
            )
        )


def get_artist_names_tidal(artist_ids: List[str], token: str) -> Optional[List[str]]:
    url = f"https://openapi.tidal.com/artists?ids={','.join(artist_ids)}&countryCode=US"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/vnd.tidal.v1+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 207:
        print("Error retrieving related artists' names from Tidal")
    else:
        return list(
            map(
                lambda artist: artist["resource"]["name"],
                response.json()["data"],
            )
        )


def get_artists_tidal(artist: str) -> Optional[Tuple[List[str], str]]:
    token = get_token()
    if token is None:
        print("No token Tidal")
        return
    data = get_artist_id_tidal(artist, token)
    if data is None:
        print("No artist id Tidal")
        return
    artist_id, artist_name = data
    related_artists_ids = get_related_artists_ids_tidal(artist_id, token)
    if related_artists_ids is None:
        print("No related artists ids from Tidal")
        return
    related_artists_names = get_artist_names_tidal(related_artists_ids, token)
    if related_artists_names is None:
        print("No related artists names from Tidal")
        return
    return related_artists_names, artist_name
