###################################
# Such discs                      #
#                  Much bounce    #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################


def get_position(num_positions, start_position, offset, time):
    position = (start_position + time + offset) % num_positions
    return position


with open("inputs/day15-1.txt") as f:
    content = f.readlines()

lines = list(map(str.strip, content))

# Process input.
discs = []
for line in lines:
    line_split = line.split(' ')
    discs.append([int(line_split[3]), int(line_split[11][:-1])])

# Manually add for Part 2.
discs.append([11, 0])

# Part 1, 2.
time = 0
part_one_found = False
while True:

    positions = list(map(lambda x: get_position(
        x[0], x[1], discs.index(x) + 1, time), discs))

    if all(x == 0 for x in positions[:-1]) and not part_one_found:
        print("Final answer for Part 1: %d" % (time))
        part_one_found = True

    if all(x == 0 for x in positions):
        print("Final answer for Part 2: %d" % (time))
        break

    time += 1
