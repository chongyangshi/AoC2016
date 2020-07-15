###################################
# Dis Python                      #
#                  Much Use       #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

KEYBOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
KEYBOARD2 = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
MOVES = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

def request_move(row_move, col_move, current_r, current_c, board_size, keyboard):

    if row_move > board_size or row_move < 0:
        return current_r, current_c
    if col_move > board_size or col_move < 0:
        return current_r, current_c
    if keyboard[row_move][col_move] is None:
        return current_r, current_c

    return row_move, col_move

with open("inputs/day2-1.txt") as f:
    content = f.read()

lines = list(content.split())
instructions = list(map(list, lines))

# Part 1, 2

for part in [1, 2]:

    current_key = 5
    passcode = ""

    if part == 1:
        current_row = 1
        current_col = 1
        board_size = 2
        keyboard = KEYBOARD
    else:
        current_row = 2
        current_col = 0
        board_size = 4
        keyboard = KEYBOARD2

    for instruction in instructions:
        for direction in instruction:
            current_row, current_col = request_move(current_row + MOVES[direction][0], current_col + MOVES[direction][1], current_row, current_col, board_size, keyboard)
        passcode += str(keyboard[current_row][current_col])

    print("Final answer for Part %d: %s" % (part, passcode))

