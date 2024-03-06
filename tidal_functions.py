# import base64
# from typing import List, Optional
# import requests
# from constants import TIDAL_CLIENT_ID, TIDAL_CLIENT_SECRET


# def get_token() -> Optional[str]:
#     url = "https://auth.tidal.com/v1/oauth2/token"
#     b4_credentials = base64.b64encode(
#         f"{TIDAL_CLIENT_ID}:{TIDAL_CLIENT_SECRET}".encode()
#     ).decode("utf-8")

#     body = {
#         "grant_type": "client_credentials",
#     }
#     headers = {
#         "Authorization": f"Basic {b4_credentials}",
#     }
#     response = requests.post(url, data=body, headers=headers)
#     if response.status_code != 200:
#         print("Error")
#     else:
#         return response.json()["access_token"]


# def get_artist_id_tidal(artist: str) -> Optional[str]:
#     token = get_token()
#     url = f"https://openapi.tidal.com/v1/search/?query={artist}&type=artist"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/vnd.tidal.v1+json",
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print("Error")
#     else:
#         return response.json()["artists"]["items"][0]["id"]
