import tkinter as tk
from gui.difficulty import DifficultyScreen


class HomeScreen:

    def __init__(self, root):

        self.root = root

        self.show_home()

    # ======================================================
    # SHOW HOME SCREEN
    # ======================================================

    def show_home(self):

        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("EscapeDS")
        self.root.geometry("900x600")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # ==================================================
        # TITLE
        # ==================================================

        tk.Label(
            self.root,
            text="ESCAPEDS",
            font=("Arial", 34, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=(100, 20))

        tk.Label(
            self.root,
            text="A Discrete Mathematics Escape Room",
            font=("Arial", 15),
            fg="#aaaaaa",
            bg="#121212"
        ).pack(pady=5)

        # ==================================================
        # START GAME
        # ==================================================

        tk.Button(
            self.root,
            text="START GAME",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.start_game
        ).pack(pady=(45, 10))

        # ==================================================
        # INSTRUCTIONS
        # ==================================================

        tk.Button(
            self.root,
            text="INSTRUCTIONS",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.show_instructions
        ).pack(pady=10)

        # ==================================================
        # EXIT
        # ==================================================

        tk.Button(
            self.root,
            text="EXIT",
            font=("Arial", 15, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.root.destroy
        ).pack(pady=10)

    # ======================================================
    # START GAME
    # ======================================================

    def start_game(self):

        # Clear Home Screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Open difficulty selection inside SAME window
        DifficultyScreen(self.root)

    # ======================================================
    # INSTRUCTIONS
    # ======================================================

    def show_instructions(self):

        instruction_window = tk.Toplevel(
            self.root
        )

        instruction_window.title(
            "EscapeDS - Instructions"
        )

        instruction_window.geometry(
            "600x400"
        )

        instruction_window.configure(
            bg="#1e1e1e"
        )

        tk.Label(
            instruction_window,
            text="INSTRUCTIONS",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=30)

        instructions = (
            "• Choose a difficulty level.\n\n"
            "• Explore the escape room.\n\n"
            "• Solve Discrete Mathematics puzzles.\n\n"
            "• Earn keys by solving puzzles.\n\n"
            "• Use keys to unlock doors.\n\n"
            "• Reach the final room and escape!"
        )

        tk.Label(
            instruction_window,
            text=instructions,
            font=("Arial", 14),
            fg="#cccccc",
            bg="#1e1e1e",
            justify="left"
        ).pack(pady=10)