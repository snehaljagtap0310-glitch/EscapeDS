from engine.inventory import Inventory


class Player:

    def __init__(self, starting_room):

        self.current_room = starting_room

        # Player inventory represented as a Set
        self.inventory = Inventory()

    def move_to(self, room):

        self.current_room = room

    def collect_item(self, item):

        self.inventory.add_item(item)

    def has_item(self, item):

        return self.inventory.has_item(item)