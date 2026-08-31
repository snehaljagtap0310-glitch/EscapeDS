import random


class KeyManager:

    def __init__(self, graph, door_manager):

        self.graph = graph
        self.door_manager = door_manager

        # Key → Room relation
        self.key_locations = {}

        # Keys that have already been collected
        self.collected_keys = set()

    def place_keys(self):

        rooms = list(self.graph.nodes())

        # Keys should not be placed in entrance or exit
        available_rooms = [
            room for room in rooms
            if room != 0 and room != len(rooms) - 1
        ]

        # Place each key in a different room
        for key_name in self.door_manager.keys:

            if available_rooms:

                room = random.choice(available_rooms)

                self.key_locations[key_name] = room

                available_rooms.remove(room)

        return self.key_locations

    def get_key_at_room(self, room):

        for key, location in self.key_locations.items():

            # Don't show keys that have already been collected
            if location == room and key not in self.collected_keys:

                return key

        return None

    def collect_key(self, key):

        if key in self.key_locations:

            self.collected_keys.add(key)

            return True

        return False