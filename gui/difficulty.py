import tkinter as tk
from engine.map_generator import MapGenerator
from gui.game import GameScreen


class DifficultyScreen:

    def __init__(self, root):

        self.root = root

        self.show_screen()

    # ======================================================
    # SHOW DIFFICULTY SCREEN
    # ======================================================

    def show_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title(
            "EscapeDS - Select Difficulty"
        )

        self.root.geometry(
            "900x600"
        )

        self.root.configure(
            bg="#121212"
        )

        # ==================================================
        # TITLE
        # ==================================================

        tk.Label(
            self.root,
            text="CHOOSE DIFFICULTY",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=(100, 30))

        # ==================================================
        # EASY
        # ==================================================

        tk.Button(
            self.root,
            text="EASY",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=lambda: self.select("Easy")
        ).pack(pady=10)

        # ==================================================
        # MEDIUM
        # ==================================================

        tk.Button(
            self.root,
            text="MEDIUM",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=lambda: self.select("Medium")
        ).pack(pady=10)

        # ==================================================
        # HARD
        # ==================================================

        tk.Button(
            self.root,
            text="HARD",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=lambda: self.select("Hard")
        ).pack(pady=10)

    # ======================================================
    # SELECT DIFFICULTY
    # ======================================================

    def select(self, level):

        print(
            "Difficulty Selected:",
            level
        )

        generator = MapGenerator(level)

        graph = generator.generate_map()

        if generator.is_solvable():

            print(
                "BFS Check: Escape room is solvable!"
            )

        else:

            print(
                "BFS Check: Escape room is NOT solvable!"
            )

        # Clear difficulty screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Open Game in SAME root
        GameScreen(
            self.root,
            level,
            graph
        )