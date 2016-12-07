###################################
# Such error                      #
#                 Many correction #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

from collections import OrderedDict

with open("inputs/day6-1.txt") as f:
    content = f.readlines()

# Part 1, 2
lines = map(str.strip, content)
# Assuming all inputs with same length, initialise dict with positions.
occurances = OrderedDict({key: {} for key in range(len(lines[0]))})

for line in lines:
    for i in range(0, len(line)):
        if line[i] in occurances[i]:
            occurances[i][line[i]] += 1
        else:
            occurances[i][line[i]] = 1

reconstructed_string1 = ""
reconstructed_string2 = ""
for position in occurances:
    most_common = max(occurances[position], key=occurances[position].get)
    least_common = min(occurances[position], key=occurances[position].get)
    reconstructed_string1 += most_common
    reconstructed_string2 += least_common

print("Final answer for Part 1: %s" % (reconstructed_string1))
print("Final answer for Part 2: %s" % (reconstructed_string2))
