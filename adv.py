from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

direction_flipped = {'w': 'e', 's': 'n', 'e': 'w', 'n': 's'}

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def travel_path(prev_rooms=[]):
    player_room = player.current_room
    d_f = direction_flipped
    prev_direction = []
# Start off by finding all of the potential exits in the player's current room,
# then move the player towards the exit.
    for direction in player_room.get_exits():
        player.travel(direction)
# If the player has not been to their current room (not in prev_rooms), 
# add it to the previous rooms list now (prev_rooms.append(player_room.id))
# also add the player's recent direction to the previous direction list 
# (prev_direction.append(direction)).
        if player.current_room.id not in prev_rooms:
            prev_direction.append(direction)
            prev_rooms.append(player_room.id)
# Add the new previous rooms to prev_direction from travel_path, then 
# move the player.
            prev_direction = prev_direction + travel_path(prev_rooms)
            player.travel(d_f[direction])
            prev_direction.append(d_f[direction])
        else:
            player.travel(d_f[direction])

    return prev_direction

traversal_path = travel_path() 

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")