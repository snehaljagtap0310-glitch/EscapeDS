import networkx as nx
import matplotlib.pyplot as plt
import random


class MapGenerator:

    def __init__(self, difficulty):

        self.difficulty = difficulty

        if difficulty == "Easy":
            self.rooms = 6

        elif difficulty == "Medium":
            self.rooms = 10

        else:
            self.rooms = 15

        self.graph = nx.Graph()

    def generate_map(self):

        # Create rooms
        for room in range(self.rooms):
            self.graph.add_node(room)

        # Connect every room with the next room
        for room in range(self.rooms - 1):
            self.graph.add_edge(room, room + 1)

        # Add some random extra connections
        extra_edges = self.rooms // 2

        while extra_edges > 0:

            a = random.randint(0, self.rooms - 1)
            b = random.randint(0, self.rooms - 1)

            if a != b and not self.graph.has_edge(a, b):
                self.graph.add_edge(a, b)
                extra_edges -= 1

        return self.graph

    def show_map(self):

        plt.figure(figsize=(8,6))

        pos = nx.spring_layout(self.graph)

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color="skyblue",
            node_size=1000,
            font_size=12
        )

        plt.title("Escape Room Map")

        plt.show()