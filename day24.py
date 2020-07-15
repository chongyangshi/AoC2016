###################################
# Such Christmas                  #
#                  Much Eve       #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

from copy import deepcopy

ORIGIN = '0'


def get_neighbours(current_map, pos, max_x, max_y):

    neighbours = []
    if max_x > pos[0] >= 1:
        if current_map[pos[1]][pos[0] - 1] != '#':
            neighbours.append((pos[0] - 1, pos[1]))
        if current_map[pos[1]][pos[0] + 1] != '#':
            neighbours.append((pos[0] + 1, pos[1]))

    if max_y > pos[1] >= 1:
        if current_map[pos[1] - 1][pos[0]] != '#':
            neighbours.append((pos[0], pos[1] - 1))
        if current_map[pos[1] + 1][pos[0]] != '#':
            neighbours.append((pos[0], pos[1] + 1))

    return neighbours


def heuristics_test(current_map, current, next, positions, found_positions, current_depth):

    depth_factor_current = current_depth ** 2
    depth_factor_next = (current_depth + 1) ** 2
    all_positions = list(positions.values())
    found_positions = [positions[i] for i in found_positions]
    remaining_positions = set(all_positions) - set(found_positions)
    total_distance_current = sum(
        [abs(i[0] - current[0]) + abs(i[1] - current[1]) for i in remaining_positions])
    total_distance_next = sum(
        [abs(i[0] - next[0]) + abs(i[1] - next[1]) for i in remaining_positions])
    if (depth_factor_current + total_distance_current) < (depth_factor_next + total_distance_next):
        return True
    else:
        return False


with open("inputs/day24-1.txt") as f:
    content = f.readlines()

lines = list(map(str.strip, content))
vent_map = [[lines[j][i]
             for i in range(len(lines[0]))] for j in range(len(lines))]
max_x = len(vent_map[0])
max_y = len(vent_map)
max_depth = 100

positions = {}
for j in range(len(vent_map)):
    for i in range(len(vent_map[j])):
        if vent_map[j][i].isdigit():
            positions[vent_map[j][i]] = (i, j)
all_positions = positions.values()
positions_count = len(positions)
positions_visited = []
positions_found = []
part_one_found = False
distance = None

# Queue: current position, current depth, positions found
target_queue = [[positions['0'], 0, []]]

# BFS with heuristics (with a long arse computing time) to find answers.
while len(target_queue) > 0:

    current_item = target_queue[0]
    current_pos = current_item[0]
    current_dep = current_item[1]
    pos_found = current_item[2]
    target_queue = target_queue[1:]
    positions_visited.append(current_pos)

    position_char = vent_map[current_pos[1]][current_pos[0]]
    if (position_char in positions):
        if (position_char not in pos_found):

            print("Found {} at a distance of {}.".format(
                position_char, current_dep))
            new_pos_found = pos_found[:]
            new_pos_found.append(position_char)

            if len(new_pos_found) >= positions_count:
                if not part_one_found:
                    print("Final answer for Part 1: {}.".format(current_dep))
                    part_one_found = True
                    new_pos_found.remove('0')
                else:
                    print("Final answer for Part 2: {}.".format(current_dep))
                    break

            current_depth_cleared = True
            for i in target_queue:
                if i[1] == current_dep:
                    current_depth_cleared = False

            if current_depth_cleared:
                positions_visited = [current_pos]
                target_queue = []

    neighbours = get_neighbours(vent_map, current_pos, max_x, max_y)
    if len(neighbours) > 0:
        for neighbour in neighbours:
            if heuristics_test(vent_map, current_pos, neighbour, positions, new_pos_found, current_dep):
                if neighbour not in positions_visited:
                    target_queue.append(
                        [neighbour, current_dep + 1, new_pos_found])
