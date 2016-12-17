###################################
# Such seventeen                  #
#                  Much prime     #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

import hashlib

GRID_SIZE = 4
DOOR_DIRECTIONS = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
DIRECTION_CHANGES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# Get input.
passcode = input("Enter your puzzle input: ")

# Build the grid and figure out where are the walls.
initial_grid = [[{'U': 1, 'D': 1, 'L': 1, 'R': 1}
                 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if i == 0:
            initial_grid[j][i]['L'] = -1
        if i == (GRID_SIZE - 1) and j != (GRID_SIZE - 1):
            initial_grid[j][i]['R'] = -1
        if j == 0:
            initial_grid[j][i]['U'] = -1
        if j == (GRID_SIZE - 1) and i != (GRID_SIZE - 1):
            initial_grid[j][i]['D'] = -1

# Queue item format: [current 2D grid, current location as a tuple,
# current path string (initially the passcode), current_depth]
search_queue = [[initial_grid, (0, 0), passcode, 0]]
part_one_found = False
accumulated_found_depth = None  # For Part 2.

while len(search_queue) > 0:

    item = search_queue[0]
    search_queue = search_queue[1:]
    current_grid = item[0]
    current_location = item[1]
    current_path = item[2]
    current_depth = item[3]

    # Found our destination.
    if (current_location == (GRID_SIZE - 1, GRID_SIZE - 1)) and not part_one_found:
        shortest_path = current_path[len(passcode):]
        print("Final answer for Part 1: %s" % (shortest_path))
        accumulated_found_depth = current_depth
        part_one_found = True
        continue

    # Keep going but always terminate a path at destination.
    elif current_location == (GRID_SIZE - 1, GRID_SIZE - 1):
        accumulated_found_depth = current_depth
        continue

    # Still not using deepcopy, since this is a deterministic structure and
    # this is faster? :)
    new_grid = [[{x: y[x] for x in y} for y in z] for z in current_grid]
    current_position = new_grid[current_location[0]][current_location[1]]
    current_status_string = hashlib.md5(
        current_path.encode('utf-8')).hexdigest()[:GRID_SIZE]

    # Figure out the new configuration with the direction lookup dict.
    for direction in range(GRID_SIZE):
        if (current_status_string[direction] in ['b', 'c', 'd', 'e', 'f']) and (current_position[DOOR_DIRECTIONS[direction]] >= 0):
            current_position[DOOR_DIRECTIONS[direction]] = 1
        elif current_position[DOOR_DIRECTIONS[direction]] >= 0:
            current_position[DOOR_DIRECTIONS[direction]] = 0
    # Probably not necessary due to implicit assign-by-reference here.
    new_grid[current_location[0]][current_location[1]] = current_position

    # For each possible way out, push the new state to queue.
    for door in current_position:
        if current_position[door] == 1:
            new_location = (current_location[
                            0] + DIRECTION_CHANGES[door][0], current_location[1] + DIRECTION_CHANGES[door][1])
            search_queue.append(
                [new_grid, new_location, current_path + door, current_depth + 1])

print("Final answer for Part 2: %d" % (accumulated_found_depth))
