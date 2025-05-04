import tkinter as tk
import random

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

class GuessTheArtistGame:
    def __init__(self, master):
        self.master = master
        master.title("🎵 Guess the Artist")

        self.score = 0
        self.song_label = tk.Label(master, text="", font=("Arial", 16))
        self.song_label.pack(pady=20)

        self.buttons = []
        for _ in range(4):
            btn = tk.Button(master, text="", font=("Arial", 14), width=30, command=lambda b=_: self.check_answer(b))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next", font=("Arial", 12), command=self.load_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.result_label.config(text="")
        self.song, self.correct_artist = random.choice(song_data)
        self.song_label.config(text=f"🎶 Who sang '{self.song}'?")
        
        choices = {self.correct_artist}
        while len(choices) < 4:
            _, artist = random.choice(song_data)
            choices.add(artist)
        choices = list(choices)
        random.shuffle(choices)

        for i, btn in enumerate(self.buttons):
            btn.config(text=choices[i], state=tk.NORMAL)

    def check_answer(self, button_index):
        selected = self.buttons[button_index].cget("text")
        if selected == self.correct_artist:
            self.result_label.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"❌ Wrong! It was {self.correct_artist}", fg="red")
        
        self.score_label.config(text=f"Score: {self.score}")

        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheArtistGame(root)
    root.mainloop()
