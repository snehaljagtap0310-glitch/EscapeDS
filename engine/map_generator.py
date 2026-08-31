import networkx as nx
import matplotlib.pyplot as plt
import random


class MapGenerator:

    def __init__(self, difficulty):

        self.difficulty = difficulty

        # ==================================================
        # NUMBER OF ROOMS
        # ==================================================

        if difficulty == "Easy":

            self.rooms = 6

        elif difficulty == "Medium":

            self.rooms = 10

        else:

            self.rooms = 15

        # ==================================================
        # CREATE GRAPH
        # ==================================================

        self.graph = nx.Graph()

        # Entrance
        self.entrance = 0

        # Exit
        self.exit = self.rooms - 1

        # ==================================================
        # DOOR REQUIREMENTS
        # ==================================================

        self.door_requirements = {}

    # ======================================================
    # GENERATE MAP
    # ======================================================

    def generate_map(self):

        # --------------------------------------------------
        # Add rooms
        # --------------------------------------------------

        for room in range(self.rooms):

            self.graph.add_node(room)

        # --------------------------------------------------
        # Main path
        # --------------------------------------------------

        # Connecting rooms in sequence guarantees
        # that there is always an escape route.

        for room in range(self.rooms - 1):

            self.graph.add_edge(
                room,
                room + 1
            )

        # --------------------------------------------------
        # Extra random doors
        # --------------------------------------------------

        extra_edges = self.rooms // 2

        while extra_edges > 0:

            a = random.randint(
                0,
                self.rooms - 1
            )

            b = random.randint(
                0,
                self.rooms - 1
            )

            if (
                a != b
                and not self.graph.has_edge(a, b)
            ):

                self.graph.add_edge(
                    a,
                    b
                )

                extra_edges -= 1

        # --------------------------------------------------
        # Create locked doors
        # --------------------------------------------------

        self.create_locked_doors()

        return self.graph

    # ======================================================
    # CREATE LOCKED DOORS
    # ======================================================

    def create_locked_doors(self):

        self.door_requirements = {}

        # --------------------------------------------------
        # Easy
        # --------------------------------------------------

        if self.difficulty == "Easy":

            # Door between Room 2 and Room 3
            self.door_requirements[
                tuple(sorted((2, 3)))
            ] = "Key 1"

            # Door between Room 4 and Room 5
            self.door_requirements[
                tuple(sorted((4, 5)))
            ] = "Key 2"

        # --------------------------------------------------
        # Medium
        # --------------------------------------------------

        elif self.difficulty == "Medium":

            self.door_requirements[
                tuple(sorted((3, 4)))
            ] = "Key 1"

            self.door_requirements[
                tuple(sorted((6, 7)))
            ] = "Key 2"

            self.door_requirements[
                tuple(sorted((8, 9)))
            ] = "Key 3"

        # --------------------------------------------------
        # Hard
        # --------------------------------------------------

        else:

            self.door_requirements[
                tuple(sorted((4, 5)))
            ] = "Key 1"

            self.door_requirements[
                tuple(sorted((7, 8)))
            ] = "Key 2"

            self.door_requirements[
                tuple(sorted((10, 11)))
            ] = "Key 3"

            self.door_requirements[
                tuple(sorted((13, 14)))
            ] = "Key 4"

    # ======================================================
    # CHECK DOOR
    # ======================================================

    def get_required_key(self, room_a, room_b):

        door = tuple(
            sorted(
                (room_a, room_b)
            )
        )

        return self.door_requirements.get(
            door
        )

    # ======================================================
    # BFS SOLVABILITY CHECK
    # ======================================================

    def is_solvable(self):

        # BFS starts from entrance
        visited = set()

        queue = [
            self.entrance
        ]

        while queue:

            current = queue.pop(0)

            # Exit reached
            if current == self.exit:

                return True

            # Already visited
            if current in visited:

                continue

            # Mark visited
            visited.add(
                current
            )

            # Explore neighbours
            for neighbour in self.graph.neighbors(
                current
            ):

                if neighbour not in visited:

                    queue.append(
                        neighbour
                    )

        return False

    # ======================================================
    # DISPLAY MAP
    # ======================================================

    def show_map(self):

        plt.figure(
            figsize=(8, 6)
        )

        pos = nx.spring_layout(
            self.graph,
            seed=42
        )

        # Draw graph
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color="skyblue",
            node_size=900,
            font_weight="bold"
        )

        # --------------------------------------------------
        # Display locked doors
        # --------------------------------------------------

        locked_edges = []

        for edge in self.door_requirements:

            if self.graph.has_edge(
                edge[0],
                edge[1]
            ):

                locked_edges.append(
                    edge
                )

        if locked_edges:

            nx.draw_networkx_edges(
                self.graph,
                pos,
                edgelist=locked_edges,
                width=3
            )

        plt.title(
            "EscapeDS - Escape Room Map"
        )

        plt.show()