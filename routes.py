from flask import render_template, request
from deezer_functions import get_artists_deezer
from lastfm_functions import get_artists_lastfm
from spotify_functions import get_artist_spotify


def homepage():
    return render_template("index.html")


def get_related_artists() -> str:
    artist = request.args["artist"]
    related_artists = {
        "deezer": get_artists_deezer(artist),
        "spotify": get_artist_spotify(artist),
        "lastfm": get_artists_lastfm(artist),
    }
    return render_template("index.html", related_artists=related_artists)
