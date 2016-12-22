###################################
# Such storage                    #
#                  Many fun       #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

from sys import exit
from copy import deepcopy


def get_visible_pairs(nodes):
    ''' Return a list of visible pairs for the node map.'''

    visible_pairs = []
    for nodeA in nodes:

        if nodes[nodeA][1] <= 0:
            continue

        for nodeB in nodes:

            if nodeA == nodeB:
                continue

            if nodes[nodeA][1] <= nodes[nodeB][2]:
                visible_pairs.append((nodeA, nodeB))

    return visible_pairs


def is_neighbouring_node(nodeA, nodeB, x_max, y_max):
    ''' Helper function to determine whether two nodes are neighbours. '''

    if (abs(nodeA[0] - nodeB[0]) == 1) and (nodeA[1] - nodeB[1] == 0):
        return True

    if (abs(nodeA[1] - nodeB[1]) == 1) and (nodeA[0] - nodeB[0] == 0):
        return True

    return False


def is_right_direction(load_from, load_to, target):
    ''' Helper function to check whether swapping loading one node into
        another would result in working towards target's direction. '''

    # Move on top of target.
    if load_from == target:
        return True

    if (load_to[0] <= load_from[0] <= target[0]) and (load_to[1] >= load_from[1] >= target[1]):
        return True
    else:
        return False

with open("inputs/day22-1.txt") as f:
    content = f.readlines()[2:]

# Process input.
lines = list(map(str.strip, content))
nodes = {}
x_max = -1
y_max = -1
for line in lines:
    line_split = [i for i in line.split(' ') if i != '']
    node_split = line_split[0].split('-')
    node_coordinates = (int(node_split[1][1:]), int(node_split[2][1:]))
    node_properties = []
    for i in range(1, 4):
        node_properties.append(int(line_split[i][:-1]))
    nodes[node_coordinates] = node_properties

    if node_coordinates[0] > x_max:
        x_max = node_coordinates[0]

    if node_coordinates[1] > y_max:
        y_max = node_coordinates[0]

# Part 1.
visible_pairs = get_visible_pairs(nodes)
print("Final answer for Part 1: {}".format(len(visible_pairs)))

# Part 2.
# The inputs I have found seem to be the same that there is no obstructing node
# in the y=0 column. Therefore it is simple to solve the second stage of movement.
# If this is not the case it gets a bit messy and this program shall just
# give up :P
for x in range(x_max):
    if nodes[(x, 0)][0] < nodes[(x_max, 0)][1]:
        print("Never expected this input due to strange things, can't work it out, sorry.")
        exit(1)
        break

# First move the empty space towards the target node.
# Find the empty node.
empty_node = (None, None)
for node in nodes:
    if nodes[node][1] == 0:
        empty_node = node[:]

# Use BFS to find the route.
target_node = (x_max, 0)
# Queue item: node state, current node, previous node, current depth
target_queue = [[nodes, empty_node, None, 0]]
already_examined_targets = []
data_node = (None, None)
depth_first_stage = None
while len(target_queue) > 0:

    current_item = target_queue[0]
    target_queue = target_queue[1:]
    nodes_state = current_item[0]
    current_node = current_item[1]
    previous_node = current_item[2]
    current_depth = current_item[3]

    if current_node == target_node:
        data_node = previous_node
        depth_first_stage = current_depth
        break

    current_pairs = get_visible_pairs(nodes_state)

    targets = [pair[0] for pair in current_pairs
               if pair[1] == current_node
               and is_neighbouring_node(pair[0], pair[1], x_max, y_max)
               and is_right_direction(pair[0], pair[1], target_node)
               and pair[0] not in already_examined_targets]

    # If the above (only walking to that corner) is possible, the below (consider
    # all directions) is not required, but just in case.
    if len(targets) == 0:
        targets = [pair[0] for pair in current_pairs
                   if pair[1] == current_node
                   and is_neighbouring_node(pair[0], pair[1], x_max, y_max)
                   and pair[0] not in already_examined_targets]

    # Perform the movement.
    if len(targets) > 0:
        for target in targets:
            new_nodes = deepcopy(nodes_state)
            new_nodes[current_node][1] += new_nodes[target][1]
            new_nodes[current_node][2] = new_nodes[
                current_node][0] - new_nodes[current_node][1]
            new_nodes[target][1] = 0
            new_nodes[target][2] = new_nodes[target][0]
            target_queue.append(
                [new_nodes, target, current_node, current_depth + 1])
            already_examined_targets.append(target)

# Now, we have where the data is now, and where the empty node (as curser) is,
# operating under the massively stupid assumption that every y=0 node is empty,
# it takes the cursor five movements to start from locating below the data node
# to finishing moving the data node one step above (x - 1, 1 closer to source)
# with the cursor again ends below the data node, it is a simple calculation to
# work out how many more steps do we need:
full_steps = 5 * data_node[0] + depth_first_stage

print("Final answer for Part 2: {}".format(full_steps))
