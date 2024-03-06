from flask import render_template, request
import requests
from deezer_functions import get_artists_deezer


def homepage():
    return render_template("index.html")


def get_related_artists() -> str:
    artist = request.args["artist"]
    related_artists = get_artists_deezer(artist)
    return render_template("index.html", related_artists=related_artists)
