import random
from engine.door import Door


class DoorManager:

    def __init__(self, graph, difficulty):

        self.graph = graph
        self.difficulty = difficulty

        # Store all doors
        self.doors = {}

        # Store keys
        self.keys = {}

    def create_doors(self):

        # Get all edges (connections between rooms)
        edges = list(self.graph.edges())

        # Number of locked doors based on difficulty
        if self.difficulty == "Easy":
            locked_count = 1

        elif self.difficulty == "Medium":
            locked_count = 2

        else:
            locked_count = 3

        # Randomly choose doors to lock
        locked_edges = random.sample(
            edges,
            min(locked_count, len(edges))
        )

        for door_id, edge in enumerate(locked_edges):

            room_a, room_b = edge

            key_name = f"Key {door_id + 1}"

            door = Door(
                door_id,
                key_name
            )

            self.doors[(room_a, room_b)] = door
            self.keys[key_name] = (room_a, room_b)

        return self.doors