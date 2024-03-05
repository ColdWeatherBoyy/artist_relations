from typing import List, Optional
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.get("/")
def homepage():
    return render_template("index.html")


@app.get("/artist")
def related_artist() -> str:
    artist = request.args["artist"]
    related_artists = find_related_artists(artist)
    return render_template("index.html", related_artists=related_artists)


def find_related_artists(artist: str) -> Optional[List[str]]:
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
        print("Error")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
