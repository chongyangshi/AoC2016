###################################
# Such Christmas                  #
#                  Much WoW       #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

DIRECTIONS = ['N', 'E', 'S', 'W']
NORTHINGS = ['S', None, 'N'] # -, 0, +
EASTINGS = ['W', None, 'E'] # -, 0, +

def change_direction(current_direction, moving):
    ''' Direction switcher with automatic wrap arounds. '''

    current = DIRECTIONS.index(current_direction)

    if moving == 'R':
        new_direction = (current + 1) % len(DIRECTIONS)
    else:
        new_direction = (current - 1) % len(DIRECTIONS)

    return DIRECTIONS[new_direction]

# Part 1.
with open("inputs/day1-1.txt") as f:
    content = f.read()

current_direction = 'N'
current_blocks_away = 0
blocks_northing = 0
blocks_easting = 0
visits = []
part_two_answer = None

moves = list(map(str.strip, content.split(",")))

for move in moves:

    move_direction = move[0]
    move_count = int(move[1:])
    current_direction = change_direction(current_direction, move_direction)

    if current_direction in NORTHINGS:
        blocks_northing_prev = blocks_northing
        offset = NORTHINGS.index(current_direction) - 1
        blocks_northing += offset * move_count
        points_visited = [(i, blocks_easting) for i in range(blocks_northing_prev+offset, blocks_northing+offset, offset)]
    else:
        blocks_easting_prev = blocks_easting
        offset = EASTINGS.index(current_direction) - 1
        blocks_easting += offset * move_count
        points_visited = [(blocks_northing, i) for i in range(blocks_easting_prev+offset, blocks_easting+offset, offset)]
    
    current_blocks_away = abs(blocks_northing) + abs(blocks_easting)

    if part_two_answer != None:
        break

    for point in points_visited:
        if point in visits:
            # Part 2 answer is found, keep going to find Part 1 answer.
            part_two_answer = "Final answer for Part 2: %d blocks away in total, first visited %d blocks in north-south direction and %d blocks in east-west direction twice." % (abs(point[0]) + abs(point[1]), point[0], point[1]) 
            break

    visits += points_visited

print("-----------------------------------------------------------------")
print("Final answer for Part 1: %d blocks away." % (current_blocks_away))
print(part_two_answer)