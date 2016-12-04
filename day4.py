###################################
# Such morining                   #
#                  Many O(n^2)?   #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

import string
from collections import Counter

ALPHABET = string.ascii_lowercase
REVERSE_ALPHABET = list(reversed(string.ascii_lowercase))


def most_common_5(strin):
    data = Counter(strin)
    commons = data.most_common(None)
    return sorted(commons, key=lambda x: (x[1], REVERSE_ALPHABET.index(x[0])))[-5:]


def rotate_letter(char, offset):
    char = char.lower()
    ind = (ALPHABET.index(char) + offset) % len(ALPHABET)
    return ALPHABET[ind]

with open("inputs/day4-1.txt") as f:
    content = f.readlines()

# Preprocessing
lines = list(map(str.strip, content))  # Precautionary in this case.
rooms = []
for line in lines:
    split = line.split('-')
    name = split[:-1]
    rest = split[-1]
    fullname = ""
    for n in name:
        fullname += n
    sector_id = int(rest.split('[')[0])
    check_sum = rest.split('[')[1][:-1]
    rooms.append([fullname, sector_id, check_sum])

# Part 1
part_one_answer = 0
valid_rooms = []
for room in rooms:
    most_commons = [i[0] for i in most_common_5(room[0])]
    if set(room[2]) == set(most_commons):
        part_one_answer += room[1]
        valid_rooms.append(room)

# Part 2
part_two_answer = None
for room in valid_rooms:

    decrypted_name = ""
    for i in room[0]:
        decrypted_name += rotate_letter(i, room[1])

    if "northpole" in decrypted_name:
        part_two_answer = room[1]
        break

print("Final answer for Part 1: %d" % (part_one_answer))
print("Final answer for Part 2: %d" % (part_two_answer))
