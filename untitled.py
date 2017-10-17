from flask import Flask
import spotipy

app = Flask(__name__)

@app.route('/')
def hello_world():
    spotify = spotipy.Spotify()
    results = spotify.search(q='artist: wicca phase springs eternal', type='artist')
    print(results)


if __name__ == '__main__':
    app.run()
