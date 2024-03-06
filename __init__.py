from flask import Flask
from routes import homepage, get_related_artists
from dotenv import load_dotenv
from tidal_functions import get_token


app = Flask(__name__)

load_dotenv()


@app.get("/")
def home():
    return homepage()


@app.get("/artist")
def related_art():
    return get_related_artists()


@app.get("/tidal")
def get_tidal_token():
    get_token()
    return "Token generated"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
