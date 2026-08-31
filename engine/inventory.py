class Inventory:

    def __init__(self):

        # Set of items collected by the player
        self.items = set()

    def add_item(self, item):

        self.items.add(item)
        print(f"Item collected: {item}")

    def has_item(self, item):

        return item in self.items

    def remove_item(self, item):

        if item in self.items:
            self.items.remove(item)

    def get_items(self):

        return self.items