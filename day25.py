###################################
# Such Christmas                  #
#                  Much End       #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

MINIMUM_IDENTIFIER = "01010101"

with open("inputs/day25-1.txt") as f:
    content = f.readlines()

lines = list(map(str.strip, content))

for line in lines:
    line_split = line.split(' ')

# Part 1.
a = 1
while True:

    registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    program_counter = 0
    output_buffer = ""

    while len(output_buffer) < len(MINIMUM_IDENTIFIER):

        line_split = lines[program_counter].split(' ')

        if line_split[0] == 'cpy':
            if line_split[1].isdigit():
                registers[line_split[2]] = int(line_split[1])
            else:
                registers[line_split[2]] = registers[line_split[1]]

        elif line_split[0] == 'inc':
            registers[line_split[1]] += 1

        elif line_split[0] == 'dec':
            registers[line_split[1]] -= 1

        elif line_split[0] == 'jnz':

            if line_split[1].isdigit():
                if int(line_split[1]) != 0:
                    program_counter += int(line_split[2])
                    continue
            else:
                if registers[line_split[1]] != 0:
                    program_counter += int(line_split[2])
                    continue

        elif line_split[0] == 'out':

            if line_split[1].isdigit():
                output_buffer += str(line_split[1])
            else:
                output_buffer += str(registers[line_split[1]])

        program_counter += 1

    if output_buffer.startswith(MINIMUM_IDENTIFIER):
        print("Final answer for Part 1: {}".format(a))
        break
    else:
        a += 1

# Part 2, thanks for reading through this set of terrible code.
print("Final answer for Part 2: press the button in the question, and Merry Christmas from your humble icydoge!")
