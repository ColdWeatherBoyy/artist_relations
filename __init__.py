from flask import Flask
from routes import homepage, get_related_artists
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()


@app.get("/")
def home():
    return homepage()


@app.get("/artist")
def related_art():
    return get_related_artists()


if __name__ == "__main__":
    app.run(port=8000, debug=True)
