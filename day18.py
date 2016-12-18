###################################
# Such traps                      #
#                  Much easy      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

ROWS = [40, 400000]
SAFE_TILE = '.'
TRAP_TILE = '^'
TRAPS = [list("^^."), list(".^^"), list("^.."), list("..^")]


def get_tile(prev_row, tile_no):

    if tile_no <= 0:
        previous_three = [SAFE_TILE, prev_row[0], prev_row[1]]
    elif tile_no >= (len(prev_row) - 1):
        previous_three = [prev_row[-2], prev_row[-1], SAFE_TILE]
    else:
        previous_three = [prev_row[tile_no - 1],
                          prev_row[tile_no], prev_row[tile_no + 1]]

    if previous_three in TRAPS:
        return '^'
    else:
        return '.'


with open("inputs/day18-1.txt") as f:
    content = f.readlines()

part = 1
for rows in ROWS:

    next_row = list(map(str.strip, content))[0]
    num_safe_tiles = next_row.count('.')
    counter = 0

    while counter < (rows - 1):
        next_row = [get_tile(next_row, i) for i in range(len(next_row))]
        num_safe_tiles += next_row.count('.')
        counter += 1

    print("Final answer for Part %d: %d" % (part, num_safe_tiles))
    part += 1
