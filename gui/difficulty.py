import tkinter as tk
from engine.map_generator import MapGenerator


class DifficultyScreen:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.title("Select Difficulty")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e1e")

        tk.Label(
            self.root,
            text="Choose Difficulty",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=40)

        tk.Button(
            self.root,
            text="Easy",
            font=("Arial", 16),
            width=20,
            command=lambda: self.select("Easy")
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Medium",
            font=("Arial", 16),
            width=20,
            command=lambda: self.select("Medium")
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Hard",
            font=("Arial", 16),
            width=20,
            command=lambda: self.select("Hard")
        ).pack(pady=10)

    def select(self, level):
        print("Difficulty Selected:", level)

        generator = MapGenerator(level)
        generator.generate_map()
        generator.show_map()