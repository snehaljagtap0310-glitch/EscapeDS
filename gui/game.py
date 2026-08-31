import tkinter as tk
from tkinter import messagebox

from gui.puzzle import PuzzleWindow


class GameScreen:

    def __init__(self, root=None, difficulty="Easy", graph=None):

        # ==================================================
        # WINDOW SETUP
        # ==================================================

        self.parent = root

        if root is None:
            self.root = tk.Tk()
        else:
            self.root = tk.Toplevel(root)

        self.root.title("EscapeDS")
        self.root.geometry("1000x700")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # ==================================================
        # GAME DATA
        # ==================================================

        self.difficulty = difficulty
        self.graph = graph

        # Generate map if not supplied
        if self.graph is None:

            from engine.map_generator import MapGenerator

            generator = MapGenerator(difficulty)
            self.graph = generator.generate_map()

            self.map_generator = generator

        else:

            # The difficulty screen generated the graph.
            # Create a generator so we can access
            # door requirements.
            from engine.map_generator import MapGenerator

            self.map_generator = MapGenerator(difficulty)

            # Generate its door requirements
            self.map_generator.graph = self.graph
            self.map_generator.create_locked_doors()

        # ==================================================
        # PLAYER
        # ==================================================

        self.current_room = 0

        # ==================================================
        # INVENTORY
        # ==================================================

        self.inventory = set()

        # ==================================================
        # SOLVED PUZZLES
        # ==================================================

        self.solved_rooms = set()

        # ==================================================
        # REQUIRED KEYS
        # ==================================================

        if difficulty == "Easy":

            self.required_keys = 2

        elif difficulty == "Medium":

            self.required_keys = 3

        else:

            self.required_keys = 4

        # ==================================================
        # EXIT
        # ==================================================

        rooms = sorted(
            self.graph.nodes
        )

        self.exit_room = rooms[-1]

        # ==================================================
        # PUZZLE ROOMS
        # ==================================================

        possible_rooms = [
            room
            for room in rooms
            if room != 0
            and room != self.exit_room
        ]

        self.puzzle_rooms = possible_rooms[
            :self.required_keys
        ]

        # ==================================================
        # DSACT TOPICS
        # ==================================================

        topics = [
            "Sets",
            "Relations",
            "Logic",
            "Graphs",
            "Automata",
            "Regex"
        ]

        self.room_topics = {}

        for index, room in enumerate(
            self.puzzle_rooms
        ):

            self.room_topics[room] = topics[
                index % len(topics)
            ]

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            self.root,
            bg="#181818",
            height=90
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="ESCAPEDS",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#181818"
        ).pack(
            side="left",
            padx=35,
            pady=20
        )

        tk.Label(
            header,
            text=f"Difficulty: {difficulty}",
            font=("Arial", 13),
            fg="#bbbbbb",
            bg="#181818"
        ).pack(
            side="right",
            padx=35
        )

        # ==================================================
        # MAIN FRAME
        # ==================================================

        main_frame = tk.Frame(
            self.root,
            bg="#121212"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        # ==================================================
        # LEFT PANEL
        # ==================================================

        info_frame = tk.Frame(
            main_frame,
            bg="#1e1e1e",
            width=300
        )

        info_frame.pack(
            side="left",
            fill="y",
            padx=(0, 20)
        )

        info_frame.pack_propagate(False)

        tk.Label(
            info_frame,
            text="PLAYER",
            font=("Arial", 14, "bold"),
            fg="#888888",
            bg="#1e1e1e"
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        self.room_label = tk.Label(
            info_frame,
            text="Room 0",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#1e1e1e"
        )

        self.room_label.pack(
            anchor="w",
            padx=25,
            pady=5
        )

        # ==================================================
        # INVENTORY
        # ==================================================

        self.inventory_label = tk.Label(
            info_frame,
            text="",
            font=("Arial", 13),
            fg="#cccccc",
            bg="#1e1e1e",
            justify="left"
        )

        self.inventory_label.pack(
            anchor="w",
            padx=25,
            pady=20
        )

        # ==================================================
        # PROGRESS
        # ==================================================

        self.progress_label = tk.Label(
            info_frame,
            text="",
            font=("Arial", 13),
            fg="#cccccc",
            bg="#1e1e1e",
            justify="left"
        )

        self.progress_label.pack(
            anchor="w",
            padx=25,
            pady=10
        )

        # ==================================================
        # RIGHT GAME PANEL
        # ==================================================

        game_frame = tk.Frame(
            main_frame,
            bg="#1e1e1e"
        )

        game_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==================================================
        # ROOM TITLE
        # ==================================================

        self.room_title = tk.Label(
            game_frame,
            text="",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#1e1e1e"
        )

        self.room_title.pack(
            pady=(35, 10)
        )

        # ==================================================
        # DESCRIPTION
        # ==================================================

        self.description_label = tk.Label(
            game_frame,
            text="",
            font=("Arial", 13),
            fg="#bbbbbb",
            bg="#1e1e1e",
            wraplength=500,
            justify="center"
        )

        self.description_label.pack(
            pady=15
        )

        # ==================================================
        # PUZZLE BUTTON
        # ==================================================

        self.puzzle_button = tk.Button(
            game_frame,
            text="Solve Puzzle",
            font=("Arial", 13, "bold"),
            width=25,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.open_puzzle
        )

        self.puzzle_button.pack(
            pady=15
        )

        # ==================================================
        # CONNECTED ROOMS
        # ==================================================

        tk.Label(
            game_frame,
            text="CONNECTED ROOMS",
            font=("Arial", 12, "bold"),
            fg="#777777",
            bg="#1e1e1e"
        ).pack(
            pady=(20, 10)
        )

        self.rooms_frame = tk.Frame(
            game_frame,
            bg="#1e1e1e"
        )

        self.rooms_frame.pack()

        # ==================================================
        # ESCAPE BUTTON
        # ==================================================

        self.escape_button = tk.Button(
            game_frame,
            text="Escape",
            font=("Arial", 13, "bold"),
            width=25,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            relief="flat",
            command=self.try_escape
        )

        self.escape_button.pack(
            pady=15
        )

        # ==================================================
        # STATUS
        # ==================================================

        self.status_label = tk.Label(
            game_frame,
            text="Explore the rooms and solve puzzles.",
            font=("Arial", 12),
            fg="#aaaaaa",
            bg="#1e1e1e",
            wraplength=500
        )

        self.status_label.pack(
            pady=15
        )

        # ==================================================
        # FIRST DISPLAY
        # ==================================================

        self.update_room()

    # ======================================================
    # UPDATE ROOM
    # ======================================================

    def update_room(self):

        room = self.current_room

        # --------------------------------------------------
        # ROOM NAME
        # --------------------------------------------------

        if room == 0:

            room_name = "Entrance"

        elif room == self.exit_room:

            room_name = "Final Room"

        else:

            room_name = f"Room {room}"

        self.room_label.config(
            text=f"Room {room}"
        )

        self.room_title.config(
            text=f"◉  {room_name}"
        )

        # --------------------------------------------------
        # DESCRIPTION
        # --------------------------------------------------

        if room == 0:

            description = (
                "You have entered EscapeDS.\n\n"
                "Explore the rooms and solve "
                "Discrete Mathematics puzzles "
                "to collect keys."
            )

        elif room == self.exit_room:

            description = (
                "🏁 FINAL ROOM\n\n"
                "The exit is here.\n"
                "Collect all required keys "
                "to escape."
            )

        elif room in self.puzzle_rooms:

            if room in self.solved_rooms:

                description = (
                    "✓ This puzzle has been solved.\n\n"
                    "You already collected the key."
                )

            else:

                topic = self.room_topics[room]

                description = (
                    f"🧩 A {topic} puzzle is waiting here.\n\n"
                    "Solve it correctly to receive a key."
                )

        else:

            description = (
                "This room contains no puzzle.\n\n"
                "Continue exploring."
            )

        self.description_label.config(
            text=description
        )

        # --------------------------------------------------
        # INVENTORY
        # --------------------------------------------------

        if not self.inventory:

            inventory_text = (
                "🎒 INVENTORY\n\n"
                "Empty"
            )

        else:

            inventory_text = (
                "🎒 INVENTORY\n\n"
                + "\n".join(
                    f"🔑 {key}"
                    for key in sorted(
                        self.inventory
                    )
                )
            )

        self.inventory_label.config(
            text=inventory_text
        )

        # --------------------------------------------------
        # PROGRESS
        # --------------------------------------------------

        self.progress_label.config(
            text=(
                "🧩 PROGRESS\n\n"
                f"Puzzles solved: "
                f"{len(self.solved_rooms)}"
                f"/{self.required_keys}\n\n"
                f"Keys collected: "
                f"{len(self.inventory)}"
                f"/{self.required_keys}"
            )
        )

        # --------------------------------------------------
        # PUZZLE BUTTON
        # --------------------------------------------------

        if (
            room in self.puzzle_rooms
            and room not in self.solved_rooms
        ):

            self.puzzle_button.config(
                state="normal",
                text=(
                    f"Solve "
                    f"{self.room_topics[room]} Puzzle"
                )
            )

        else:

            self.puzzle_button.config(
                state="disabled",
                text="Puzzle Completed"
            )

        # --------------------------------------------------
        # CLEAR ROOM BUTTONS
        # --------------------------------------------------

        for widget in self.rooms_frame.winfo_children():

            widget.destroy()

        # --------------------------------------------------
        # CONNECTED ROOMS
        # --------------------------------------------------

        connected_rooms = sorted(
            self.graph.neighbors(room)
        )

        for next_room in connected_rooms:

            required_key = (
                self.map_generator.get_required_key(
                    room,
                    next_room
                )
            )

            # ----------------------------------------------
            # Button text
            # ----------------------------------------------

            if required_key:

                button_text = (
                    f"🔒 Room {next_room}\n"
                    f"Requires {required_key}"
                )

            else:

                button_text = (
                    f"Go to Room {next_room}"
                )

            # ----------------------------------------------
            # Create button
            # ----------------------------------------------

            tk.Button(
                self.rooms_frame,
                text=button_text,
                font=("Arial", 11),
                width=28,
                height=2,
                bg="#292929",
                fg="white",
                activebackground="#3a3a3a",
                activeforeground="white",
                relief="flat",
                command=lambda r=next_room:
                self.move_player(r)
            ).pack(
                pady=4
            )

        # --------------------------------------------------
        # ESCAPE BUTTON
        # --------------------------------------------------

        if room == self.exit_room:

            self.escape_button.config(
                state="normal"
            )

        else:

            self.escape_button.config(
                state="disabled"
            )

    # ======================================================
    # MOVE PLAYER
    # ======================================================

    def move_player(self, room):

        # --------------------------------------------------
        # Make sure connection exists
        # --------------------------------------------------

        if not self.graph.has_edge(
            self.current_room,
            room
        ):

            self.status_label.config(
                text="You cannot move there."
            )

            return

        # --------------------------------------------------
        # Check door requirement
        # --------------------------------------------------

        required_key = (
            self.map_generator.get_required_key(
                self.current_room,
                room
            )
        )

        # --------------------------------------------------
        # Locked door
        # --------------------------------------------------

        if required_key:

            if required_key not in self.inventory:

                messagebox.showwarning(
                    "Door Locked",
                    "🔒 This door is locked!\n\n"
                    f"You need {required_key} "
                    "to enter this room.",
                    parent=self.root
                )

                self.status_label.config(
                    text=(
                        f"🔒 Door locked. "
                        f"Requires {required_key}."
                    )
                )

                return

            else:

                self.status_label.config(
                    text=(
                        f"🔓 {required_key} used. "
                        f"Door unlocked!"
                    )
                )

        # --------------------------------------------------
        # Move player
        # --------------------------------------------------

        self.current_room = room

        print(
            f"Player moved to Room {room}"
        )

        self.update_room()

    # ======================================================
    # OPEN PUZZLE
    # ======================================================

    def open_puzzle(self):

        room = self.current_room

        if room not in self.puzzle_rooms:

            return

        if room in self.solved_rooms:

            return

        topic = self.room_topics[room]

        print(
            f"Opening {topic} puzzle "
            f"in Room {room}"
        )

        PuzzleWindow(
            self.root,
            topic=topic,
            on_solved=lambda r=room:
            self.puzzle_solved(r)
        )

    # ======================================================
    # PUZZLE SOLVED
    # ======================================================

    def puzzle_solved(self, room):

        # Prevent duplicate reward
        if room in self.solved_rooms:

            return

        # Mark solved
        self.solved_rooms.add(
            room
        )

        # Give key
        key_number = len(
            self.inventory
        ) + 1

        key_name = f"Key {key_number}"

        self.inventory.add(
            key_name
        )

        print(
            f"Puzzle solved in Room {room}"
        )

        print(
            f"{key_name} added to inventory"
        )

        self.status_label.config(
            text=(
                f"🎉 Puzzle solved!\n"
                f"🔑 {key_name} added to inventory."
            )
        )

        self.update_room()

        # ======================================================
    # ESCAPE
    # ======================================================

    def try_escape(self):

        # Make sure player is at exit room
        if self.current_room != self.exit_room:
            return

        # --------------------------------------------------
        # Check whether all keys are collected
        # --------------------------------------------------

        if len(self.inventory) < self.required_keys:

            remaining = (
                self.required_keys
                - len(self.inventory)
            )

            messagebox.showwarning(
                "Exit Locked",
                "🚪 The exit is locked!\n\n"
                f"You still need {remaining} key(s).",
                parent=self.root
            )

            self.status_label.config(
                text=(
                    f"🔒 Exit locked. "
                    f"Find {remaining} more key(s)."
                )
            )

            return

        # --------------------------------------------------
        # SUCCESS
        # --------------------------------------------------

        messagebox.showinfo(
            "Escape Successful!",
            "🎉 CONGRATULATIONS!\n\n"
            "You solved the puzzles,\n"
            "collected all the keys,\n"
            "and escaped EscapeDS!",
            parent=self.root
        )

        print("PLAYER ESCAPED!")

        # --------------------------------------------------
        # Import Result Screen
        # --------------------------------------------------

        from gui.result import ResultScreen

        # --------------------------------------------------
        # Clear the current GAME screen
        # --------------------------------------------------

        for widget in self.root.winfo_children():
            widget.destroy()

        # --------------------------------------------------
        # Open RESULT screen
        # --------------------------------------------------

        ResultScreen(
            self.root,
            self.difficulty,
            len(self.inventory),
            self.required_keys,
            len(self.solved_rooms),
            self.required_keys
        )

    # ======================================================
    # RUN
    # ======================================================

    def run(self):

        self.root.mainloop()