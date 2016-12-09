###################################
# Such chaos                      #
#                 Many rewrites   #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

with open("inputs/day9-1.txt") as f:
    content = f.readlines()

data = list(content[0].strip())

# Part 1.
processing_marker = False
remaining_length = 0
multiplier = 1
multiplying = ""
output = ""
numbers = []

# Simple parsing and tallying.
for char in data:

    if char == '(' and remaining_length <= 0:
        output += multiplying
        processing_marker = True
        multiplier = 1
        multiplying = ""
    elif char == 'x' and processing_marker:
        remaining_length = int(''.join(numbers))
        numbers = []
    elif char == ')' and processing_marker:
        processing_marker = False
        multiplier = int(''.join(numbers))
        numbers = []
    elif char.isdigit() and processing_marker:
        numbers.append(char)
    elif not processing_marker:
        multiplying += char
        remaining_length -= 1

    if remaining_length == 0:
        output += multiplying * multiplier
        multiplying = ""
        multiplier = 1

output += multiplying * multiplier  # What's left.

# Part 2.
processing_marker = False
multiplying_length = 0
multipliers = [1 for i in data]

# Parse the input data and record the correct multiplier for each character.
for char in range(len(data)):

    if data[char] == '(':
        processing_marker = True
    elif data[char] == 'x' and processing_marker:
        multiplying_length = int(''.join(numbers))
        numbers = []
    elif data[char].isdigit() and processing_marker:
        numbers.append(data[char])
    elif data[char] == ')' and processing_marker:
        processing_marker = False
        multiplier = int(''.join(numbers))
        for i in range(char + 1, char + 1 + multiplying_length):
            multipliers[i] *= multiplier
        numbers = []

total_length = 0
for char in range(len(data)):
    if data[char].isupper():  # Excluding all markers.
        total_length += multipliers[char]


print("Final answer for Part 1: %d" % (len(output)))
print("Final answer for Part 2: %d" % (total_length))
