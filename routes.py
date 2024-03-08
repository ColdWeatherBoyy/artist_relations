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
    related_artists = {}
    deezer_artists = get_artists_deezer(artist)
    if deezer_artists:
        related_artists["deezer"] = deezer_artists
    spotify_artists = get_artist_spotify(artist)
    if spotify_artists:
        related_artists["spotify"] = spotify_artists
    tidal_artists = get_artists_tidal(artist)
    if tidal_artists:
        related_artists["tidal"] = tidal_artists
    lastfm_artists = get_artists_lastfm(artist)
    if lastfm_artists:
        related_artists["lastfm"] = lastfm_artists
    related_artists_ranked, platform_count = compare_artists(related_artists)
    return render_template(
        "index.html",
        related_artists_ranked=related_artists_ranked,
        platform_count=platform_count,
    )
