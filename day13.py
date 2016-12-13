###################################
# Such number                     #
#                  Much maze      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

# Board size.
X = 31
Y = 39
X_Target = 31
Y_Target = 39
PART_TWO_LOCATIONS = 50

puzzle_input = int(input("Enter your puzzle input: "))

num_values = [[puzzle_input + x*x + 3*x + 2*x*y + y + y*y for x in range(X + 2)] for y in range(Y + 2)]

for y in range(Y + 2):
    for x in range(X + 2):
        one_count = bin(num_values[y][x])[2:].count('1')
        if one_count % 2 == 0:
            num_values[y][x] = 1
        else:
            num_values[y][x] = -1

# Point, previous distance.
routing_queue = [[(1,1), 0]]
visited_points = []
part_two_reached = 0

# BFS Search to find closest distance.
while len(routing_queue) > 0:

    current_point = routing_queue[0][0]
    current_distance = routing_queue[0][1]
    routing_queue = routing_queue[1:]

    x = current_point[0]
    y = current_point[1]

    # At destination.
    if (X_Target == x) and (Y_Target == y):
        print("Final answer for Part 1: %d" % (current_distance))
        break

    # No repeat visiting.
    if current_point in visited_points:
        continue
    else:
        visited_points.append(current_point)
        if current_distance <= 50:
            part_two_reached += 1

    # Add new route points, sorry for the ugly code.
    if x > 0:
        if num_values[y][x-1] > 0:
            routing_queue.append([(x-1, y), current_distance + 1])
    if y > 0:
        if num_values[y-1][x] > 0:
            routing_queue.append([(x, y-1), current_distance + 1])
    if x < X:
        if num_values[y][x+1] > 0:
            routing_queue.append([(x+1, y), current_distance + 1])
    if y < Y:
        if num_values[y+1][x] > 0:
            routing_queue.append([(x, y+1), current_distance + 1])

print("Final answer for Part 2: %d" % (part_two_reached))
