from flask import json, render_template, request
from helper_functions.deezer_functions import get_artists_deezer
from helper_functions.general_helper_functions import (
    compare_artists,
    evaluate_platform,
    sort_artists_by_rank,
)
from helper_functions.lastfm_functions import get_artists_lastfm
from helper_functions.spotify_functions import get_artist_spotify
from helper_functions.tidal_functions import get_artists_tidal


def homepage():
    return render_template("index.html")


def get_related_artists() -> str:
    artist = request.args["artist"]
    related_artists = {}

    # evaluate each platform and add the related artists to the related_artists dictionary
    evaluate_platform(artist, get_artist_spotify, "Spotify", related_artists)
    evaluate_platform(artist, get_artists_lastfm, "Last.fm", related_artists)
    evaluate_platform(artist, get_artists_deezer, "Deezer", related_artists)
    evaluate_platform(artist, get_artists_tidal, "Tidal", related_artists)

    # compare the related artists from each platform and return the results
    related_artists_ranked, platform_count = compare_artists(related_artists)

    # sort the related artists by how many playforms that are found in
    sorted_related_artists = sort_artists_by_rank(related_artists_ranked)

    return render_template(
        "index.html",
        sorted_related_artists=sorted_related_artists,
        platform_count=platform_count,
    )
