###################################
# Such strings                    #
#                  Much rotate    #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

SOURCE_1 = "abcdefgh"
SOURCE_2 = "fbgdceah"

with open("inputs/day21-1.txt") as f:
    content = f.readlines()

lines_part_one = list(map(str.strip, content))
lines_part_two = list(map(str.strip, reversed(content)))

# Part 1.
op_string = SOURCE_1
for line in lines_part_one:

    line_split = line.split(' ')
    current_string = list(op_string)

    if line_split[0] == "swap":

        if line_split[1] == "position":
            temp = op_string[int(line_split[5])]
            current_string[int(line_split[5])] = op_string[int(line_split[2])]
            current_string[int(line_split[2])] = temp

        else:
            for i in range(0, len(op_string)):
                if op_string[i] == line_split[5]:
                    current_string[i] = line_split[2]
                elif op_string[i] == line_split[2]:
                    current_string[i] = line_split[5]

    elif line_split[0] == "rotate":

        # Compute the negative offset for rotation.
        if line_split[1] == "left":
            offset = -1 * int(line_split[2])
        elif line_split[1] == "right":
            offset = 1 * int(line_split[2])
        elif line_split[1] == "based":
            offset = op_string.index(line_split[6])
            if offset >= 4:
                offset += 2
            else:
                offset += 1

        for i in range(0, len(op_string)):
            rotate_position = (i - offset) % len(op_string)
            current_string[i] = op_string[rotate_position]

    elif line_split[0] == "reverse":

        reverse_from = int(line_split[2])
        reverse_to = int(line_split[4])

        for i in range(reverse_from, reverse_to + 1):
            location = reverse_to + reverse_from - i
            current_string[i] = op_string[location]

    elif line_split[0] == "move":

        from_location = int(line_split[2])
        to_location = int(line_split[5])
        letter = op_string[from_location]
        current_string = op_string[:from_location] + \
            op_string[(from_location + 1):]
        current_string = current_string[
            :to_location] + letter + current_string[to_location:]

    op_string = ''.join(current_string)

print("Final answer for Part 1: {}".format(op_string))

# Part 2.
op_string = SOURCE_2
for line in lines_part_two:

    line_split = line.split(' ')
    current_string = list(op_string)

    if line_split[0] == "swap":
        if line_split[1] == "position":
            temp = op_string[int(line_split[2])]
            current_string[int(line_split[2])] = op_string[int(line_split[5])]
            current_string[int(line_split[5])] = temp
        else:
            for i in range(0, len(op_string)):
                if op_string[i] == line_split[5]:
                    current_string[i] = line_split[2]
                elif op_string[i] == line_split[2]:
                    current_string[i] = line_split[5]

    elif line_split[0] == "rotate":

        if line_split[1] == "left":
            offset = int(line_split[2])
            for i in range(0, len(op_string)):
                rotate_position = (i - offset) % len(op_string)
                current_string[i] = op_string[rotate_position]

        elif line_split[1] == "right":
            offset = int(line_split[2])
            for i in range(0, len(op_string)):
                rotate_position = (i + offset) % len(op_string)
                current_string[i] = op_string[rotate_position]

        # Brute force search of the correct original string, after an hour of
        # effort in vain.
        elif line_split[1] == "based":
            strings_to_test = []

            for n in range(len(op_string)):

                testing_string = current_string[:]

                for i in range(len(op_string)):
                    rotate_position = (i + n) % len(op_string)
                    testing_string[i] = op_string[rotate_position]

                strings_to_test.append(testing_string)

            for testing_string in strings_to_test:

                offset = testing_string.index(line_split[6])
                check_string = testing_string[:]

                if offset >= 4:
                    offset += 2
                else:
                    offset += 1

                for i in range(0, len(testing_string)):
                    rotate_position = (i - offset) % len(testing_string)
                    check_string[i] = testing_string[rotate_position]

                if check_string == current_string:
                    current_string = testing_string[:]
                    break

    elif line_split[0] == "reverse":

        reverse_from = int(line_split[2])
        reverse_to = int(line_split[4])

        for i in range(reverse_from, reverse_to + 1):
            location = reverse_to + reverse_from - i
            current_string[i] = op_string[location]

    elif line_split[0] == "move":

        from_location = int(line_split[5])
        to_location = int(line_split[2])
        letter = op_string[from_location]

        current_string = op_string[:from_location] + \
            op_string[(from_location + 1):]
        current_string = current_string[
            :to_location] + letter + current_string[to_location:]

    op_string = ''.join(current_string)

print("Final answer for Part 2: {}".format(op_string))
