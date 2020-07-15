###################################
# Such number                     #
#                  Much firewall  #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

IP_MIN = 0
IP_MAX = 4294967295

with open("inputs/day20-1.txt") as f:
    content = f.readlines()

# Process input into range of constraints.
lines = list(map(str.strip, content))
constraints = []
for line in lines:
    line_split = list(map(int, line.split('-')))
    constraints.append((line_split[0], line_split[1]))

# First sort the constraints into a blacklist by lower bound.
blacklist = sorted(constraints, key=lambda x: x[0])

# Then we can merge overlapping blacklist ranges.
i = 0
while i < (len(blacklist) - 1):

    # A merge possible.
    if blacklist[i][1] >= blacklist[i + 1][0] - 1:

        # Entirely covering the next one, delete next.
        if blacklist[i][1] >= blacklist[i + 1][1]:
            del blacklist[i + 1]

        # Only partially covering the next one, merge the two.
        else:
            blacklist[i] = (blacklist[i][0], blacklist[i + 1][1])
            del blacklist[i + 1]

    # Current one fully merged, moving on to the next one.
    else:
        i += 1

# Easily grab our answers.
min_available = blacklist[0][1] + 1
available_ips = sum([blacklist[i + 1][0] - blacklist[i][1] - 1 for i in range(0, len(blacklist) - 1)])

print("Final answer for Part 1: {}".format(min_available))
print("Final answer for Part 2: {}".format(available_ips))
