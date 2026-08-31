import tkinter as tk


class ResultScreen:

    def __init__(
        self,
        parent,
        difficulty,
        keys_collected,
        total_keys,
        puzzles_solved,
        total_puzzles
    ):

        self.parent = parent

        self.window = tk.Toplevel(parent)

        self.window.title("EscapeDS - Results")
        self.window.geometry("900x600")
        self.window.configure(bg="#121212")
        self.window.resizable(False, False)

        # Keep result window in front
        self.window.transient(parent)
        self.window.grab_set()

        # ==================================================
        # TITLE
        # ==================================================

        tk.Label(
            self.window,
            text="🎉 ESCAPE SUCCESSFUL!",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=(60, 15))

        tk.Label(
            self.window,
            text="Congratulations! You escaped EscapeDS.",
            font=("Arial", 17),
            fg="#cccccc",
            bg="#121212"
        ).pack(pady=10)

        # ==================================================
        # RESULT BOX
        # ==================================================

        result_frame = tk.Frame(
            self.window,
            bg="#1e1e1e"
        )

        result_frame.pack(
            pady=25,
            ipadx=70,
            ipady=20
        )

        tk.Label(
            result_frame,
            text=f"Difficulty: {difficulty}",
            font=("Arial", 14),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=7)

        tk.Label(
            result_frame,
            text=f"🔑 Keys Collected: {keys_collected}/{total_keys}",
            font=("Arial", 14),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=7)

        tk.Label(
            result_frame,
            text=f"🧩 Puzzles Solved: {puzzles_solved}/{total_puzzles}",
            font=("Arial", 14),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=7)

        # ==================================================
        # PLAY AGAIN
        # ==================================================

        tk.Button(
            self.window,
            text="PLAY AGAIN",
            font=("Arial", 13, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.play_again
        ).pack(pady=6)

        # ==================================================
        # MAIN MENU
        # ==================================================

        tk.Button(
            self.window,
            text="MAIN MENU",
            font=("Arial", 13, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.main_menu
        ).pack(pady=6)

        # ==================================================
        # EXIT
        # ==================================================

        tk.Button(
            self.window,
            text="EXIT",
            font=("Arial", 13, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.exit_game
        ).pack(pady=6)

    # ======================================================
    # PLAY AGAIN
    # ======================================================

    def play_again(self):

        self.window.grab_release()
        self.window.destroy()

        # Open difficulty selection
        from gui.difficulty import DifficultyScreen

        DifficultyScreen(self.parent)

    # ======================================================
    # MAIN MENU
    # ======================================================

    def main_menu(self):

        self.window.grab_release()
        self.window.destroy()

        # Close the game window
        try:
            self.parent.destroy()
        except:
            pass

        # Open Home Screen
        from gui.home import HomeScreen

        HomeScreen()

    # ======================================================
    # EXIT
    # ======================================================

    def exit_game(self):

        try:
            self.window.grab_release()
        except:
            pass

        self.window.destroy()

        try:
            self.parent.destroy()
        except:
            pass