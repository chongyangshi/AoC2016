###################################
# Such steal                      #
#                  Much hard      #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################


def get_next_available_elf(presents, start, fixed_length):

    count = 0

    while count < (fixed_length + 1):
        count += 1
        location = (start + count) % fixed_length
        if presents[location] > 0:
            return location

    return None


elves = int(input("Enter your puzzle input: "))

# Part 1.
presents = [1 for i in range(elves)]
current_elf = 0
lucky_elf = None
current_none_zero_length = elves

while True:

    if presents[current_elf] > 0:

        steal_from = get_next_available_elf(presents, current_elf, elves)

        if steal_from == current_elf:
            lucky_elf = current_elf
            break

        presents[current_elf] += presents[steal_from]
        presents[steal_from] = 0
        current_none_zero_length -= 1

    current_elf = (current_elf + 1) % elves

print("Final answer for Part 1: %d" % (lucky_elf + 1))

# Part 2, analytical method stolen from Numberphile.
elves_groups = 1
while elves_groups * 3 < elves:
    elves_groups *= 3

print("Final answer for Part 2: %d" % (elves - elves_groups))
