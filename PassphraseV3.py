#!/usr/bin/python3

'''
Version 3 of Passphrase Generator. This update was created on 3 February, 2025
Created by Alayna Ferdarko.
Version 3 of the Passphrase Generator comes packed with 303-words! But if you read the readme.txt, you already know this...
'''

import tkinter as tk
from tkinter import messagebox
import random
import os

# Sample words for passphrase generation
WORDS = [
"sunset", "mountain", "ocean", "forest", "river", "cloud", "storm",
"whisper", "shadow", "echo", "flame", "dream", "spark", "breeze",
"stone", "meadow", "wave", "sky", "fire", "light", "galaxy", "comet",
"nebula", "planet", "star", "orbit", "cosmos",
"meteor", "asteroid", "eclipse", "quasar", "horizon", "dawn",
"twilight", "glimmer", "prism", "crystal", "vortex", "void",
"cascade", "tempest", "frost", "ember", "blaze", "aurora", "chasm",
"abyss", "rapids", "delta", "peak", "ridge", "valley", "summit",
"grove", "thicket", "canopy", "brook", "canyon", "dune", "lagoon",
"reef", "glacier", "cavern", "tundra", "savanna", "desert", "mesa",
"plateau", "arch", "spire", "crown", "bluff", "haven", "oasis",
"sanctuary", "enclave", "bastion", "citadel", "fortress", "stronghold",
"realm", "kingdom", "empire", "province", "village",
"hamlet", "settlement", "outpost", "camp", "pavilion", "tent",
"shack", "cottage", "lodge", "villa", "manor", "palace", "castle",
"tower", "keep", "dungeon", "crypt", "labyrinth", "maze", "portal",
"gate", "passage", "corridor", "hall", "chamber", "sanctum",
"temple", "shrine", "monument", "obelisk", "statue", "idol",
"relic", "artifact", "tome", "scroll", "manuscript", "map",
"compass", "beacon", "signal", "flare", "lantern", "torch",
"candle", "lamp", "glow", "radiance", "luster", "gleam",
"shine", "beam", "ray", "arc", "ring", "circle", "sphere",
"orb", "disk", "plate", "fragment", "shard", "sliver", "chip",
"pebble", "boulder", "rock", "gem", "jewel", "diamond", "ruby",
"sapphire", "emerald", "topaz", "amber", "wolf",
"raven", "computer", "gavel", "grave", "sign", "nexus", "knife",
"penguin", "fox", "lion", "sandcat", "opossum",
"giraffe", "shark", "whale", "raptor", "zephyr", "zenith", "zany", "zealous",
"zink", "alpha", "foxtrot", "bravo", "charlie", "golf", "hotel", "india",
"juliette", "kilo", "lima", "november", "oscar", "mike",
"romeo", "papa", "quebec", "sierra", "tango", "uniform", "victor", "whiskey", "xray",
"yankee", "zulu", "winter", "autumn", "summer", "spring", "warfare", "wale",
"walm", "wallet", "wack", "wadmal", "wafture", "wallflower", "wamus",
"barracks", "commander", "squadron", "fortification", "recon", "ambush",
"armory", "infantry", "bunker", "militia", "artillery", "platoon", "tactics",
"maneuver", "strategy", "checkpoint", "battlefield", "victory", "trooper",
"assault", "mission", "defense", "warrant", "regiment", "bravery", "flag",
"alliance", "strike", "frontline", "revolt", "taurus", "scorpio", "libra",
"aries", "capricorn", "aquarius", "leo", "gemini", "virgo", "cancer", "sagittarius",
"pisces", "mercury", "venus", "earth", "jupiter", "mars", "saturn", "uranus", "neptune",
"sun", "moon", "elephant", "giraffe", "zebra", "panda", "koala", "lemur", "platypus",
"armadillo", "walrus", "sloth", "crocodile", "alligator", "hippopotamus", "raccoon",
"moose", "peacock",  "ostrich", "otter", "cheeta", "hyena", "jackal", "meerkat", "buffalo",
"anteater", "manatee", "bison", "wolverine", "chinchilla", "bee", "wasp", "hornet", "bat"
]

class PassphraseGenerator:
    FILE_PATH = "liked_passphrases.txt"

    def __init__(self, root):
        self.root = root
        self.root.title("Passphrase Generator v.3 by Alayna Ferdarko")
        
        # Locks for keeping parts of the passphrase
        self.locks = [False, False, False]

        # Current passphrase parts
        self.passphrase_parts = ["", "", ""]

        # Load saved passphrases
        self.saved_passphrases = self.load_saved_passphrases()

        # Frame for the slot machine display
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.labels = []
        self.lock_buttons = []
        
        # Create display labels and lock buttons
        for i in range(3):
            frame = tk.Frame(self.display_frame)
            frame.pack(side=tk.LEFT, padx=10)

            label = tk.Label(frame, text="", font=("Consolas", 24), width=10, relief="solid")
            label.pack()
            self.labels.append(label)

            lock_button = tk.Button(frame, text="Unlock", command=lambda idx=i: self.toggle_lock(idx))
            lock_button.pack(pady=5)
            self.lock_buttons.append(lock_button)

        # Spin button
        self.spin_button = tk.Button(self.root, text="Spin", font=("Consolas", 16), command=self.spin)
        self.spin_button.pack(pady=20)

        # Like button
        self.like_button = tk.Button(self.root, text="Like", font=("Consolas", 16), command=self.like)
        self.like_button.pack(pady=10)

        # Saved passphrases button
        self.show_saved_button = tk.Button(self.root, text="Show Saved", font=("Consolas", 16), command=self.show_saved)
        self.show_saved_button.pack(pady=10)

    def spin(self):
        """Generates a new passphrase."""
        for i in range(3):
            if not self.locks[i]:
                self.passphrase_parts[i] = random.choice(WORDS)
                self.labels[i].config(text=self.passphrase_parts[i])

    def toggle_lock(self, idx):
        """Toggles the lock for a specific part of the passphrase."""
        self.locks[idx] = not self.locks[idx]
        self.lock_buttons[idx].config(text="Lock" if self.locks[idx] else "Unlock")

    def like(self):
        """Saves the current passphrase to a file."""
        passphrase = " ".join(self.passphrase_parts)
        if passphrase and passphrase not in self.saved_passphrases:
            self.saved_passphrases.append(passphrase)
            with open(self.FILE_PATH, "a") as file:
                file.write(passphrase + "\n")
            messagebox.showinfo("Saved", "Passphrase saved: " + passphrase)
        else:
            messagebox.showinfo("Info", "Passphrase already saved!")

    def show_saved(self):
        """Displays the saved passphrases."""
        if self.saved_passphrases:
            saved = "\n".join(self.saved_passphrases)
            messagebox.showinfo("Saved Passphrases", saved)
        else:
            messagebox.showinfo("Saved Passphrases", "No passphrases saved yet.")

    def load_saved_passphrases(self):
        """Loads previously saved passphrases from a file."""
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

if __name__ == "__main__":
    root = tk.Tk()
    app = PassphraseGenerator(root)
    root.mainloop()
