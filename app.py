from flask import Flask, request, render_template_string
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Spotify API credentials (store safely in production!)
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Load tracks once (you could cache or randomize further)
playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M'
playlist_id = playlist_url.split("/")[-1].split("?")[0]
tracks = sp.playlist_tracks(playlist_id)['items']
quiz_data = [(t['track']['name'], t['track']['artists'][0]['name']) for t in tracks if t['track']]

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        guess = request.form["guess"]
        song = request.form["song"]
        artist = request.form["artist"]
        correct = guess.strip().lower() == artist.lower()
        result = "Correct!" if correct else f"Wrong! The artist was: {artist}"
    else:
        song, artist = random.choice(quiz_data)
        result = ""

    return render_template_string('''
        <h1>Guess the Artist</h1>
        <p>Which artist sang the song: <b>{{ song }}</b>?</p>
        <form method="post">
            <input type="hidden" name="song" value="{{ song }}">
            <input type="hidden" name="artist" value="{{ artist }}">
            <input type="text" name="guess" placeholder="Your guess">
            <button type="submit">Submit</button>
        </form>
        <p>{{ result }}</p>
    ''', song=song, artist=artist, result=result)

if __name__ == "__main__":
    app.run(debug=True)
