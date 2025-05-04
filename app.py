import tkinter as tk
import random

# Sample song database
song_data = [
    ("Blinding Lights", "The Weeknd"),
    ("Bohemian Rhapsody", "Queen"),
    ("Billie Jean", "Michael Jackson"),
    ("Lose Yourself", "Eminem"),
    ("Rolling in the Deep", "Adele"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Uptown Funk", "Mark Ronson"),
    ("Someone Like You", "Adele"),
    ("Hey Jude", "The Beatles"),
    ("Take a Walk", "Passion Pit"),
    ("Electric Feel", "MGMT"),
    ("Sweet Disposition", "The Temper Trap"),
    ("Holocene", "Bon Iver"),
    ("The Less I Know the Better", "Tame Impala"),
    ("Sedona", "Houndmouth"),
    ("Tennessee Whiskey", "Chris Stapleton"),
    ("Broken Halos", "Chris Stapleton"),
    ("Feathered Indians", "Tyler Childers"),
    ("All Your'n", "Tyler Childers"),
    ("Something in the Orange", "Zach Bryan"),
    ("Burn, Burn, Burn", "Zach Bryan"),
    ("Iris", "The Goo Goo Dolls"),
    ("Yellow", "Coldplay"),
    ("Kiss Me", "Sixpence None The Richer"),
    ("Girl Crush - Recorded at Metropolis Studios, London", "Harry Styles"),
    ("Starman - 2012 Remaster", "David Bowie"),
    ("Movin' Out (Anthony's Song)", "Billy Joel"),
    ("Youngest Daughter", "Superheaven"),
    ("Glory Box", "Portishead"),
    ("Sparks", "Coldplay"),
    ("Vienna", "Billy Joel"),
    ("Charlie Brown", "Coldplay"),
    ("Slow Dancing in a Burning Room", "John Mayer"),
    ("Sign of the Times", "Harry Styles"),
    ("Linger", "The Cranberries"),
    ("Do It Again", "Steely Dan"),
    ("Lovefool", "The Cardigans"),
    ("Something Like Olivia", "John Mayer"),
    ("Need 2", "Pinegrove"),
    ("Hunger Strike", "Temple Of The Dog"),
    ("Song 2 - 2012 Remaster", "Blur"),
    ("Push", "Matchbox Twenty"),
    ("Alive", "Pearl Jam"),
    ("One Last Breath", "Creed"),
    ("Everlong", "Foo Fighters"),
    ("Animal - Remastered", "Pearl Jam"),
    ("Rearviewmirror - Remastered", "Pearl Jam"),
    ("Wheels", "Foo Fighters"),
    ("This Velvet Glove", "Red Hot Chili Peppers"),
    ("Sometimes", "My Bloody Valentine"),
    ("Breathe (In the Air)", "Pink Floyd"),
    ("Kickstart My Heart", "Mötley Crüe"),
    ("My Sacrifice", "Creed"),
    ("Drive", "Incubus"),
    ("3AM", "Matchbox Twenty"),
    ("Dani California", "Red Hot Chili Peppers"),
    ("Be Quiet and Drive (Far Away)", "Deftones"),
    ("Elderly Woman Behind the Counter in a Small Town - Remastered", "Pearl Jam"),
    ("Sex on Fire", "Kings of Leon"),
    ("Street Spirit (Fade Out)", "Radiohead"),
    ("High and Dry", "Radiohead"),
    ("Silver Springs - 2004 Remaster", "Fleetwood Mac"),
    ("Cry For The Bad Man", "Lynyrd Skynyrd"),
    ("Hazel - 2024 Remaster", "Far Apart"),
    ("Don't Look Back In Anger - Remastered", "Oasis"),
    ("Hello - Remastered", "Oasis"),
    ("Roll With It - Remastered", "Oasis"),
    ("Take Me Out", "Franz Ferdinand"),
    ("Like a Prayer", "Madonna"),
    ("Country House - 2012 Remaster", "Blur"),
    ("Use Somebody", "Kings of Leon"),
    ("About You", "The 1975"),
    ("Easy Lover", "Philip Bailey, Phil Collins"),
    ("Come Sail Away", "Styx"),
    ("Sister Golden Hair", "America"),
    ("Take Me Home Tonight", "Eddie Money")
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
