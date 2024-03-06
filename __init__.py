from flask import Flask
from routes import homepage, get_related_artists


app = Flask(__name__)


@app.get("/")
def home():
    return homepage()


@app.get("/artist")
def related_art():
    return get_related_artists()


if __name__ == "__main__":
    app.run(port=8000, debug=True)
