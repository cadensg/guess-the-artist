from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Sample song database
song_data = [
    ("Shape of You", "Ed Sheeran"),
    ("Blinding Lights", "The Weeknd"),
    ("Bohemian Rhapsody", "Queen"),
    ("Billie Jean", "Michael Jackson"),
    ("Lose Yourself", "Eminem"),
    ("Rolling in the Deep", "Adele"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Uptown Funk", "Mark Ronson"),
    ("Someone Like You", "Adele"),
    ("Hey Jude", "The Beatles")
]

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        guess = request.form["guess"]
        correct = request.form["correct"]
        if guess == correct:
            result = "✅ Correct!"
        else:
            result = f"❌ Wrong! The correct artist was: {correct}"
    else:
        result = ""

    song, correct_artist = random.choice(song_data)

    # Generate multiple choices
    choices = {correct_artist}
    while len(choices) < 4:
        _, other_artist = random.choice(song_data)
        choices.add(other_artist)
    choices = list(choices)
    random.shuffle(choices)

    return render_template_string('''
        <h1>🎵 Guess the Artist</h1>
        <p>Which artist sang the song: <b>{{ song }}</b>?</p>
        <form method="post">
            <input type="hidden" name="correct" value="{{ correct_artist }}">
            {% for choice in choices %}
                <button type="submit" name="guess" value="{{ choice }}">{{ choice }}</button><br><br>
            {% endfor %}
        </form>
        <p>{{ result }}</p>
    ''', song=song, correct_artist=correct_artist, choices=choices, result=result)

if __name__ == "__main__":
    app.run(debug=True)
