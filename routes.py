from flask import json, render_template, request
from helper_functions.deezer_functions import get_artists_deezer
from helper_functions.general_helper_functions import compare_artists
from helper_functions.lastfm_functions import get_artists_lastfm
from helper_functions.spotify_functions import get_artist_spotify
from helper_functions.tidal_functions import get_artists_tidal


def homepage():
    return render_template("index.html")


def get_related_artists() -> str:
    artist = request.args["artist"]
    related_artists = {
        "deezer": get_artists_deezer(artist),
        "spotify": get_artist_spotify(artist),
        "lastfm": get_artists_lastfm(artist),
        "tidal": get_artists_tidal(artist),
    }
    related_artists_ranked = compare_artists(related_artists)
    return render_template("index.html", related_artists_ranked=related_artists_ranked)
