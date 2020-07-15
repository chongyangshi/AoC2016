###################################
# Such MD5                        #
#                  Much Collision #
#       Very Movie Doge           #
###################################
# By C Shi <icydoge@gmail.com>  #
# Adapted from Day 4 of 2015.     #
###################################


import hashlib

input_string = input("Enter puzzle input: ")

# Part 1,2
number = 0
found1 = 0
password1 = list("********")
password2 = list("********")
print("1cyD0g3 is 'decrypting' the door passwords: ********, ********.", end='\r')

while True:
    current_string = input_string + str(number)
    new_hash = hashlib.md5(current_string.encode('utf-8')).hexdigest()

    if new_hash.startswith("00000"):

        if found1 < 8:
            password1[found1] = new_hash[5]
            found1 += 1
            print("1cyD0g3 is 'decrypting' the door passwords: %s, %s." %
                  (''.join(password1), ''.join(password2)), end='\r')

        if new_hash[5].isdigit():
            potential_position = int(new_hash[5])
            if (0 <= potential_position <= 7) and password2[potential_position] == '*':
                password2[potential_position] = str(new_hash[6])
                print("1cyD0g3 is 'decrypting' the door passwords: %s, %s." %
                      (''.join(password1), ''.join(password2)), end='\r')

        if found1 >= 8 and '*' not in password2:
            break

    number += 1

print("")
print("Final answer for Part 1: %s" % (''.join(password1)))
print("Final answer for Part 2: %s" % (''.join(password2)))
