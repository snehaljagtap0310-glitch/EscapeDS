import tkinter as tk
from gui.difficulty import DifficultyScreen


class HomeScreen:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("EscapeDS")

        self.root.geometry("900x600")

        self.root.configure(bg="#1e1e1e")

        # Title
        title = tk.Label(
            self.root,
            text="EscapeDS",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#1e1e1e"
        )

        title.pack(pady=40)

        # Start Game Button
        start_btn = tk.Button(
            self.root,
            text="Start Game",
            font=("Arial", 16),
            width=20,
            command=self.start_game
        )

        start_btn.pack(pady=10)

        # Instructions Button
        instruction_btn = tk.Button(
            self.root,
            text="Instructions",
            font=("Arial", 16),
            width=20,
            command=self.show_instructions
        )

        instruction_btn.pack(pady=10)

        # Exit Button
        exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Arial", 16),
            width=20,
            command=self.root.destroy
        )

        exit_btn.pack(pady=10)

    # Open Difficulty Screen
    def start_game(self):
        DifficultyScreen()

    # Temporary Instructions Window
    def show_instructions(self):
        instruction_window = tk.Toplevel(self.root)
        instruction_window.title("Instructions")
        instruction_window.geometry("600x400")
        instruction_window.configure(bg="#1e1e1e")

        tk.Label(
            instruction_window,
            text="Instructions",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=20)

        instructions = (
            "• Choose a difficulty level.\n\n"
            "• Explore the escape room.\n\n"
            "• Solve Discrete Mathematics puzzles.\n\n"
            "• Collect keys and unlock doors.\n\n"
            "• Escape before the timer ends!"
        )

        tk.Label(
            instruction_window,
            text=instructions,
            font=("Arial", 14),
            fg="white",
            bg="#1e1e1e",
            justify="left"
        ).pack(pady=10)

    def run(self):
        self.root.mainloop()