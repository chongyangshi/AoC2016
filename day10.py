###################################
# Such digits                     #
#                  Much Two       #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

import sys

# The two values being looked for, VALUE_1 < VALUE_2.
VALUE_1 = 17
VALUE_2 = 61

# Otherwise infinite loop will happen.
if VALUE_1 >= VALUE_2:
    sys.exit("Invalid values to look for in script constants.")


with open("inputs/day10-1.txt") as f:
    content = f.readlines()


# Part 1, 2.
lines = [line.split(' ') for line in content]
bot_lines = [line for line in lines if line[0] == 'bot']
source_lines = [line for line in lines if line[0] == 'value']
bots = {}
outputs = {}
still_on_bots = 0

for line in bot_lines:

    source_bot = int(line[1])
    lower_desitination = int(line[6])
    higher_desitination = int(line[11])
    lower_type = line[5]
    higher_type = line[10]
    bots[source_bot] = {
        'lower_desitination': lower_desitination,
        'higher_desitination': higher_desitination,
        'chips_held': [],
        'lower_type': lower_type,
        'higher_type': higher_type
    }

for line in source_lines:

    source_value = int(line[1])
    destination = int(line[5])
    bots[destination]['chips_held'].append(source_value)
    still_on_bots += 1

bot_processing = None

while True:

    # Repeat until all chips have been shifted to outputs.
    for bot in bots:

        if sorted(bots[bot]['chips_held']) == [VALUE_1, VALUE_2] and bot_processing is None:
            # Check for Part 1, still finishing transactions for Part 2.
            bot_processing = bot

        if len(bots[bot]['chips_held']) == 2:
            # Do transactions.
            if bots[bot]['lower_type'] == "output":
                outputs[bots[bot]['lower_desitination']] = min(
                    bots[bot]['chips_held'])
                still_on_bots -= 1
            else:
                bots[bots[bot]['lower_desitination']][
                    'chips_held'].append(min(bots[bot]['chips_held']))

            if bots[bot]['higher_type'] == "output":
                outputs[bots[bot]['higher_desitination']] = max(
                    bots[bot]['chips_held'])
                still_on_bots -= 1
            else:
                bots[bots[bot]['higher_desitination']][
                    'chips_held'].append(max(bots[bot]['chips_held']))

            bots[bot]['chips_held'] = []

    if still_on_bots <= 0:
        break

print("Final answer for Part 1: %d" % (bot_processing))
print("Final answer for Part 2: %d" % (outputs[0] * outputs[1] * outputs[2]))
