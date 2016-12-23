###################################
# Such assembly                   #
#                  Much repeat    #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

ADD_LOOP = ["cpy", "inc", "dec", "jnz", "dec", "jnz"]


def is_number(n):
    ''' Due to isdigit()'s annoyances with negative numbers. '''
    try:
        int(n)
        return True

    except ValueError:
        return False


def find_add_loop(lines, registers):
    ''' Helper function to check whether the next six lines
        is an add loop, returns new register state if yes. '''

    line_instructions = [a[:3] for a in lines]

    if line_instructions == ADD_LOOP:
        multiply1 = lines[0].split(' ')[1]
        multiply2 = lines[4].split(' ')[1]
        incremented_register = lines[1].split(' ')[1]
        cleared_register = lines[2].split(' ')[1]
        registers[incremented_register] += registers[multiply1] * \
            registers[multiply2]
        registers[multiply2] = 0
        registers[cleared_register] = 0
        return registers

    else:
        return False


with open("inputs/day23-1.txt") as f:
    content = f.readlines()

# Part 1 (a = 7), 2 (a = 12).
for bunnies in [7, 12]:

    lines = list(map(str.strip, content))
    registers = {'a': bunnies, 'b': 0, 'c': 0, 'd': 0}
    program_counter = 0

    while program_counter < len(lines):

        line_split = lines[program_counter].split(' ')

        if line_split[0] == 'cpy' and len(line_split) == 3:

            if not is_number(line_split[2]):

                # If it's an add loop, calculate multiply and skip it.
                if not is_number(line_split[1]):
                    loop_test = find_add_loop(
                        lines[program_counter: (program_counter + 6)], registers)
                    if loop_test:
                        registers = loop_test
                        program_counter += 6
                        continue

                # Otherwise copy normally.
                if is_number(line_split[1]):
                    registers[line_split[2]] = int(line_split[1])
                else:
                    registers[line_split[2]] = registers[line_split[1]]

        elif line_split[0] == 'inc' and len(line_split) == 2:
            if not is_number(line_split[1]):
                registers[line_split[1]] += 1

        elif line_split[0] == 'dec' and len(line_split) == 2:
            if not is_number(line_split[1]):
                registers[line_split[1]] -= 1

        elif line_split[0] == 'jnz' and len(line_split) == 3:

            if is_number(line_split[1]):
                if int(line_split[1]) != 0:
                    if is_number(line_split[2]):
                        program_counter += int(line_split[2])
                        continue
                    elif line_split[2] in registers:
                        program_counter += registers[line_split[2]]
                        continue
            else:
                if registers[line_split[1]] != 0:
                    if is_number(line_split[2]):
                        program_counter += int(line_split[2])
                        continue
                    elif line_split[2] in registers:
                        program_counter += registers[line_split[2]]
                        continue

        elif line_split[0] == 'tgl' and len(line_split) == 2:

            # Both numbers and registers can be used in tgl, apparently.
            if is_number(line_split[1]):
                toggle_pc = program_counter + int(line_split[1])
            else:
                toggle_pc = program_counter + registers[line_split[1]]

            if 0 <= toggle_pc < len(lines):
                # One argument target.
                if len(lines[toggle_pc].split(' ')) == 2:
                    if lines[toggle_pc].startswith('inc'):
                        lines[toggle_pc] = 'dec' + lines[toggle_pc][3:]
                    else:
                        lines[toggle_pc] = 'inc' + lines[toggle_pc][3:]
                # Two argument target.
                else:
                    if lines[toggle_pc].startswith('jnz'):
                        lines[toggle_pc] = 'cpy' + lines[toggle_pc][3:]
                    else:
                        lines[toggle_pc] = 'jnz' + lines[toggle_pc][3:]

        program_counter += 1

    print("Final answer for Part {}: {}".format(
        [7, 12].index(bunnies) + 1, registers['a']))
