from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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

player = Player('Brian', room['outside'].room_name, room['outside'].room_description)
print(player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def set_player_direction(player):
    print(player.room_name)
    print(player.room_description)
    setting_direction = True
    while setting_direction:
        try:
            direction = input("Enter a direction [n, s, e, w] ")
            if direction == "n":
                setting_direction = False
                print(direction)
                return direction
            elif direction == "s":
                setting_direction = False
                print(direction)
                return direction
            elif direction == "e":
                setting_direction = False
                print(direction)
                return direction
            elif direction == "w":
                setting_direction = False
                print(direction)
                return direction
        except ValueError:
            print("You must enter one of the following directions [n, s, e, w] ")


set_player_direction(player)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
