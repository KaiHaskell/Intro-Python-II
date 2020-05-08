from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
                     """
            Dim light filters in from the south. Dusty
            passages run north and east.
    """),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'counterfeit gold coin': Item("Counterfeit Gold Coin", "You found a gold coin! Unfortunately it's fake, and therefore useless."),
    'rusty sword': Item("Rusty Sword", "It looks like it might snap in two from one hit."),
    'pair of jorts': Item("Pair of Jorts", "It accentuates your thighs."),
    'egg': Item("Egg", "It's an egg.")
}

# Link items to rooms
room['outside'].addItem(item['rusty sword'])
room['foyer'].addItem(item['pair of jorts'])
room['treasure'].addItem(item['counterfeit gold coin'])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

username = input("What is your name? ")
newPlayer = Player(username, room['outside'], inventory=[])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

active = True

while active:
    # Every time the loop is initiated, the description of the room must be given as well as it's name
    print(
        f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
               Player: [{newPlayer.name}]               
               Location: [{newPlayer.location.name}]
             ══════════════════════════════════════════
             {newPlayer.location.description}
        '''
    )
    # A list of all actions a user can take within a given room
    action = input(
        '''              
                          Choose an option.
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃    [n] North [s] South [e] East [w] West            ┃
        ┃    [i] Inventory [take item] [drop item]            ┃
        ┃    [q] Quit                                         ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        ''').lower()
    inputs = action.split()
    # If the user enters "q", quit the game.
    if action == "q":
        print(f'See you next time')
        active = False
    elif action in ['n', 's', 'e', 'w']:
        newPlayer.move_to(action, newPlayer.location)
    else:
        print("This is not a valid input.\n")
