import base64
from typing import List, Optional
import requests
from constants import TIDAL_CLIENT_ID, TIDAL_CLIENT_SECRET


def get_token() -> Optional[str]:
    url = "https://auth.tidal.com/v1/oauth2/token"
    b4_credentials = base64.b64encode(
        f"{TIDAL_CLIENT_ID}:{TIDAL_CLIENT_SECRET}".encode()
    ).decode("utf-8")

    body = {
        "grant_type": "client_credentials",
    }
    headers = {
        "Authorization": f"Basic {b4_credentials}",
    }
    response = requests.post(url, data=body, headers=headers)
    if response.status_code != 200:
        print("Error")
    else:
        return response.json()["access_token"]
