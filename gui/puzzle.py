import tkinter as tk
from tkinter import messagebox
import random


class PuzzleWindow:

    def __init__(self, parent, topic="Sets", on_solved=None):

        self.parent = parent
        self.topic = topic
        self.on_solved = on_solved

        # ==================================================
        # CREATE PUZZLE WINDOW
        # ==================================================

        self.window = tk.Toplevel(parent)

        self.window.title("EscapeDS - Puzzle")
        self.window.geometry("850x600")
        self.window.configure(bg="#121212")
        self.window.resizable(False, False)

        # Keep puzzle in front
        self.window.transient(parent)
        self.window.grab_set()

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.close_puzzle
        )

        # ==================================================
        # QUESTION BANK
        # ==================================================

        self.questions = {

            "Sets": [

                {
                    "question":
                    "If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∪ B?",

                    "options": [
                        "{1, 2, 3}",
                        "{3, 4, 5}",
                        "{1, 2, 3, 4, 5}",
                        "{1, 2, 5}"
                    ],

                    "answer": 2
                },

                {
                    "question":
                    "If A = {1, 2, 3} and B = {2, 3}, what is A − B?",

                    "options": [
                        "{1}",
                        "{2, 3}",
                        "{1, 2}",
                        "{3}"
                    ],

                    "answer": 0
                }

            ],

            "Relations": [

                {
                    "question":
                    "Which relation is reflexive on A = {1, 2}?",

                    "options": [
                        "{(1,1), (2,2)}",
                        "{(1,2)}",
                        "{(2,1)}",
                        "{(1,2), (2,1)}"
                    ],

                    "answer": 0
                },

                {
                    "question":
                    "A relation R is symmetric if:",

                    "options": [
                        "aRb implies bRa",
                        "aRb implies aRa",
                        "aRb implies bRb",
                        "aRb never occurs"
                    ],

                    "answer": 0
                }

            ],

            "Logic": [

                {
                    "question":
                    "What is the negation of the statement: 'All students passed'?",

                    "options": [
                        "No student passed",
                        "At least one student did not pass",
                        "All students failed",
                        "Some students passed"
                    ],

                    "answer": 1
                },

                {
                    "question":
                    "If P is True and Q is False, what is P AND Q?",

                    "options": [
                        "True",
                        "False",
                        "Both",
                        "Undefined"
                    ],

                    "answer": 1
                }

            ],

            "Graphs": [

                {
                    "question":
                    "In graph theory, vertices are connected by:",

                    "options": [
                        "Sets",
                        "Edges",
                        "Relations",
                        "Matrices"
                    ],

                    "answer": 1
                },

                {
                    "question":
                    "A graph with no cycles is called:",

                    "options": [
                        "Complete graph",
                        "Cyclic graph",
                        "Acyclic graph",
                        "Directed graph"
                    ],

                    "answer": 2
                }

            ],

            "Automata": [

                {
                    "question":
                    "DFA stands for:",

                    "options": [
                        "Dynamic Finite Algorithm",
                        "Deterministic Finite Automaton",
                        "Data Flow Automaton",
                        "Directed Finite Algorithm"
                    ],

                    "answer": 1
                },

                {
                    "question":
                    "A DFA has:",

                    "options": [
                        "Multiple transitions for the same input",
                        "Exactly one transition for each state-input pair",
                        "No states",
                        "Only one state"
                    ],

                    "answer": 1
                }

            ],

            "Regex": [

                {
                    "question":
                    "Which symbol represents zero or more repetitions in regular expressions?",

                    "options": [
                        "+",
                        "?",
                        "*",
                        "^"
                    ],

                    "answer": 2
                },

                {
                    "question":
                    "Which regular expression represents one or more 'a' characters?",

                    "options": [
                        "a*",
                        "a+",
                        "a?",
                        "a^"
                    ],

                    "answer": 1
                }

            ]

        }

        # ==================================================
        # SELECT QUESTION
        # ==================================================

        topic_questions = self.questions.get(
            self.topic,
            self.questions["Sets"]
        )

        self.current_question = random.choice(
            topic_questions
        )

        self.selected_answer = tk.IntVar(
            value=-1
        )

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.window,
            bg="#181818",
            height=80
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="ESCAPEDS",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#181818"
        ).pack(
            side="left",
            padx=30,
            pady=20
        )

        tk.Label(
            header,
            text=f"PUZZLE • {self.topic.upper()}",
            font=("Arial", 13, "bold"),
            fg="#aaaaaa",
            bg="#181818"
        ).pack(
            side="right",
            padx=30
        )

        # ==================================================
        # MAIN CONTENT
        # ==================================================

        content = tk.Frame(
            self.window,
            bg="#1e1e1e"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        tk.Label(
            content,
            text="Solve the puzzle to obtain the key",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(
            pady=(20, 30)
        )

        # ==================================================
        # QUESTION
        # ==================================================

        tk.Label(
            content,
            text=self.current_question["question"],
            font=("Arial", 15),
            fg="white",
            bg="#1e1e1e",
            wraplength=700,
            justify="center"
        ).pack(
            pady=15
        )

        # ==================================================
        # OPTIONS
        # ==================================================

        options_frame = tk.Frame(
            content,
            bg="#1e1e1e"
        )

        options_frame.pack(
            pady=20
        )

        for index, option in enumerate(
            self.current_question["options"]
        ):

            tk.Radiobutton(
                options_frame,
                text=option,
                variable=self.selected_answer,
                value=index,
                font=("Arial", 13),
                fg="white",
                bg="#1e1e1e",
                activebackground="#1e1e1e",
                activeforeground="white",
                selectcolor="#333333",
                anchor="w",
                width=40
            ).pack(
                pady=6
            )

        # ==================================================
        # SUBMIT
        # ==================================================

        self.submit_button = tk.Button(
            content,
            text="SUBMIT ANSWER",
            font=("Arial", 13, "bold"),
            width=22,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.check_answer
        )

        self.submit_button.pack(
            pady=20
        )

        # ==================================================
        # STATUS
        # ==================================================

        self.status_label = tk.Label(
            content,
            text="Choose an answer and submit.",
            font=("Arial", 11),
            fg="#888888",
            bg="#1e1e1e"
        )

        self.status_label.pack(
            pady=5
        )

    # ======================================================
    # CHECK ANSWER
    # ======================================================

    def check_answer(self):

        selected = self.selected_answer.get()

        # --------------------------------------------------
        # No answer
        # --------------------------------------------------

        if selected == -1:

            messagebox.showwarning(
                "No Answer",
                "Please select an answer first.",
                parent=self.window
            )

            return

        correct = self.current_question["answer"]

        # ==================================================
        # CORRECT ANSWER
        # ==================================================

        if selected == correct:

            # Disable submit button
            self.submit_button.config(
                state="disabled"
            )

            self.status_label.config(
                text="✓ Correct! Key unlocked!",
                fg="lightgreen"
            )

            messagebox.showinfo(
                "Correct!",
                "🎉 Correct answer!\n\n"
                "You obtained a key.",
                parent=self.window
            )

            # --------------------------------------------------
            # Release modal grab
            # --------------------------------------------------

            try:

                self.window.grab_release()

            except tk.TclError:

                pass

            # --------------------------------------------------
            # Destroy puzzle window FIRST
            # --------------------------------------------------

            try:

                self.window.destroy()

            except tk.TclError:

                pass

            # --------------------------------------------------
            # Tell GameScreen AFTER puzzle is destroyed
            # --------------------------------------------------

            if self.on_solved:

                try:

                    self.parent.after(
                        50,
                        self.on_solved
                    )

                except tk.TclError:

                    pass

        # ==================================================
        # WRONG ANSWER
        # ==================================================

        else:

            self.status_label.config(
                text="✗ Incorrect! Try again.",
                fg="#ff7777"
            )

            messagebox.showerror(
                "Incorrect",
                "❌ Wrong answer!\n\n"
                "Try again.",
                parent=self.window
            )

    # ======================================================
    # CLOSE PUZZLE
    # ======================================================

    def close_puzzle(self):

        result = messagebox.askyesno(
            "Leave Puzzle?",
            "If you leave now, you will not get the key.\n\n"
            "Are you sure?",
            parent=self.window
        )

        if result:

            try:

                self.window.grab_release()

            except tk.TclError:

                pass

            self.window.destroy()