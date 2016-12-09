###################################
# Such lights                     #
#                 Many lines      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

# Size of the grid.
COLUMNS = 50
ROWS = 6


def shift_column(grid, at, by):

    if not 0 <= at < COLUMNS:
        return grid

    new_grid = [row[:] for row in grid]

    for y in range(0, ROWS):
        new_y = (y + by) % ROWS
        new_grid[new_y][at] = grid[y][at]

    return new_grid


def shift_row(grid, at, by):

    if not 0 <= at < ROWS:
        return grid

    new_grid = [row[:] for row in grid]

    for x in range(0, COLUMNS):
        new_x = (x + by) % COLUMNS
        new_grid[at][new_x] = grid[at][x]

    return new_grid


with open("inputs/day8-1.txt") as f:
    content = f.readlines()

lines = map(str.strip, content)
grid = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

for line in lines:

    line_split = line.split(' ')

    if line_split[0] == 'rect':

        turn_on = line_split[1].split('x')
        turn_on_x = int(turn_on[0])
        turn_on_y = int(turn_on[1])

        for y in range(0, turn_on_y):
            for x in range(0, turn_on_x):
                grid[y][x] = 1

    elif line_split[0] == 'rotate':

        shift_by = line_split[2].split('=')
        shift_at_n = int(shift_by[1])
        shift_by_n = int(line_split[4])

        if shift_by[0] == 'x':
            grid = shift_column(grid, shift_at_n, shift_by_n)
        else:
            grid = shift_row(grid, shift_at_n, shift_by_n)


lit_pixels = 0

for y in grid:
    for x in y:
        if x == 1:
            lit_pixels += 1
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print("Final answer for Part 1: %d" % (lit_pixels))
print("Final answer for Part 2: Please read from the grid above.")
