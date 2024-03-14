from flask import Flask, render_template, request
from .routes import homepage, get_related_artists
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

port = int(os.getenv("PORT", 8000))


@app.get("/")
def home():
    return homepage()


@app.get("/artist")
def related_art():
    return get_related_artists()


env = os.getenv("ENV")

if __name__ == "__main__":
    if env == "production":
        app.run(host="0.0.0.0", port=port)
    elif env == "development":
        app.run(port=port, debug=True)
