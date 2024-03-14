from collections import defaultdict
from flask import render_template, request
from helper_functions.deezer_functions import get_artists_deezer
from helper_functions.general_helper_functions import (
    compare_and_sort_artists,
    evaluate_platform,
)
from helper_functions.lastfm_functions import get_artists_lastfm
from helper_functions.spotify_functions import get_artist_spotify
from helper_functions.tidal_functions import get_artists_tidal


def homepage():
    return render_template("index.html")


def get_related_artists() -> str:
    artist = request.args["artist"]
    related_artists = {}
    artist_name_dict = defaultdict(lambda: 0)

    # evaluate each platform and add the related artists to the related_artists dictionary
    evaluate_platform(
        artist, get_artist_spotify, "Spotify", related_artists, artist_name_dict
    )
    evaluate_platform(
        artist, get_artists_lastfm, "Last.fm", related_artists, artist_name_dict
    )
    evaluate_platform(
        artist, get_artists_deezer, "Deezer", related_artists, artist_name_dict
    )
    evaluate_platform(
        artist, get_artists_tidal, "Tidal", related_artists, artist_name_dict
    )

    # compare and sort the related artists from each platform and return the results
    related_artists, platforms = compare_and_sort_artists(related_artists)

    # Find which spelling of artist name is most common
    most_used_artist_name = max(artist_name_dict.keys())

    return render_template(
        "index.html",
        artist=most_used_artist_name,
        related_artists=related_artists,
        platforms=platforms,
    )
