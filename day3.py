###################################
# Many lines                      #
#                  Such O(n)      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

with open("inputs/day3-1.txt") as f:
    content = f.readlines()

# Part 1
lines = list(map(str.strip, content))
triangles = []
for line in lines:
    split = line.split(' ')
    triangles.append([int(i) for i in split if i != ''])

valid = 0
for triangle in triangles:
    if (triangle[0] + triangle[1]) > triangle[2] and (triangle[1] + triangle[2]) > triangle[0] and (triangle[0] + triangle[2]) > triangle[1]:
        valid += 1

print("Final answer for Part 1: %d" % (valid))

# Part 2
triangles2 = []
for i in range(0, len(triangles) - 2, 3):
    for j in range(0, 3):
        triangles2.append([triangles[i][j], triangles[i + 1][j], triangles[i + 2][j]])

valid = 0
for triangle in triangles2:
    if (triangle[0] + triangle[1]) > triangle[2] and (triangle[1] + triangle[2]) > triangle[0] and (triangle[0] + triangle[2]) > triangle[1]:
        valid += 1

print("Final answer for Part 2: %d" % (valid))
