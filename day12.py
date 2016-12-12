###################################
# Such micro                      #
#                  Much code      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################


with open("inputs/day12-1.txt") as f:
    content = f.readlines()

lines = list(map(str.strip, content))

for i in range(0, 2):

    registers = {'a': 0, 'b': 0, 'c': i, 'd': 0}
    program_counter = 0

    while program_counter < len(lines):

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

        program_counter += 1

    print("Final answer for Part %d: %d" % (i + 1, registers['a']))
