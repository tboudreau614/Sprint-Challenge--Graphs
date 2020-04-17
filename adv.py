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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# Define the possible 'forward moves'
nextMovePossible = {'n': 'e', 'e': 's', 's': 'w', 'w': None }

# Define the possible 'backwards moves'
moveBack = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e' }

steps = ['n']

while len(steps) > 0: 
    # Define 'move' as equal to steps 'minus' the last step logged (deleting last step)
    move = steps.pop()
    player.travel(move)
    if player.current_room not in visited_rooms:
        # If the current room that the player is in has not been visited, move forward/backwards and 
        # add that to the end of traversal path and steps, then add the player's current room to visited rooms.
        traversal_path.append(moveBack[move])
        steps.append(moveBack[move])
        visited_rooms.add(player.current_room)

    for newMove in ['n', 'e', 's', 'w']:
        newRoom = player.current_room.get_room_in_direction(newMove)
        if newRoom and newRoom not in visited_rooms:
            # If the player's newest room has not been visited yet, add the newest move to the
            # end of the traversal path and steps. 
            traversal_path.append(newMove)
            steps.append(newMove)
            break

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: Hey wow good job bud! You did it in {len(traversal_path)} moves and visited all {len(visited_rooms)} rooms!")
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
