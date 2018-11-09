from item import Item
from player import Player
from room import Room

room = {
    'outside': Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].items = ['sword', 'wand', 'shield']

# items = {
#     'sword': Item('sword').get_item(),
#     'wand': Item('wand').get_item(),
#     'treasure': Item('treasure').get_item()
# }
#
# p1 = Player('Brian', 'outside', [])
# p1.items.append(items['sword'])
#
# print(p1)


def play_game():

    player_name = input("Player name >> ").strip()
    player = Player(player_name, 'outside')
    invalid_option = "Invalid direction"
    while True:
        print("\n")
        print("Room: " + room[player.room].name)
        print("Description: " + room[player.room].description)
        print("Items: " + ', '.join(room[player.room].items))
        print("Player Items: " + ', '.join(player.items))
        print("\n")

        choice = input("Choose a direction to travel, press q to quit, i for inventory, weapon name to pick up,"
                       " [drop item_name] to drop item in different room >> ").strip().lower()
        print(choice.split())

        # Quit Game
        if choice == 'q':
            break
        # Drop item in whatever room you are in
        if choice.split()[0] == 'drop' and choice.split()[1] in player.items:
            player.items.remove(choice.split()[1])
            room[player.room].items.append(choice.split()[1])

        # Add item to inventory from room
        if choice in room[player.room].items:
            room[player.room].items.remove(choice)
            player.items.append(choice)

        if choice in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
            # Outside to Foyer
            if player.room == 'outside' and choice[0][0] == 'n':
                player.room = 'foyer'
            elif player.room == 'outside' and choice[0][0] != 'n':
                print(invalid_option)
            # Foyer to Outside
            elif player.room == 'foyer' and choice[0][0] == 's':
                player.room = 'outside'
            # Foyer to Overlook
            elif player.room == 'foyer' and choice[0][0] == 'n':
                player.room = 'overlook'
            # Foyer to Narrow
            elif player.room == 'foyer' and choice[0][0] == 'e':
                player.room = 'narrow'
            elif player.room == 'foyer' and choice[0][0] == 'w':
                print(invalid_option)
            # Overlook to Foyer
            elif player.room == 'overlook' and choice[0][0] == 's':
                player.room = 'foyer'
            elif player.room == 'overlook' and choice[0][0] in ['n', 'e', 'w', 'north', 'east', 'west']:
                print(invalid_option)
            # Narrow to Foyer
            elif player.room == 'narrow' and choice[0][0] == 'w':
                player.room = 'foyer'
            # Narrow to Treasure
            elif player.room == 'narrow' and choice[0][0] == 'n':
                player.room = 'treasure'
            elif player.room == 'narrow' and choice[0][0] in ['n', 'w', 'north', 'west']:
                print(invalid_option)
            # Treasure to Narrow
            elif player.room == 'treasure' and choice[0][0] == 's':
                player.room = 'narrow'

play_game()
