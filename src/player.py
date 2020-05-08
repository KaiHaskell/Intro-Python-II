# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory=None):
        self.name = name
        self.location = location

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def move_to(self, direction, current_loc):
        # Attempt to move in the specified direction
        attribute = direction + '_to'
        next_location = getattr(current_loc, attribute)
        if hasattr(current_loc, attribute):
            self.location = next_location

        else:
            print("You can't go that way.")

        return current_loc

    def pickItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item)
