# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.description = description
        self.name = name
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        if items is None:
            self.items = []
        else:
            self.items = items

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
