class Door:

    def __init__(self, door_id, required_key):

        self.door_id = door_id
        self.required_key = required_key
        self.locked = True

    def can_open(self, inventory):

        # Predicate:
        # Door opens only if player has the required key
        if inventory.has_item(self.required_key):

            return True

        return False

    def unlock(self, inventory):

        if self.can_open(inventory):

            self.locked = False
            return True

        return False