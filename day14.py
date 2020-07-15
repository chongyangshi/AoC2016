###################################
# Such times                      #
#                  Much effort    #
#       Very Doge                 #
###################################
# By C Shi <icydoge@gmail.com>  #
###################################

import hashlib


class Hasher:
    ''' An object to wrap the key generation, to ensure that the same salt + sequence 
        number is hashed only ever once (otherwise performance would be bad). '''

    def __init__(self, input_string):

        self.__hash_list = {}
        self._input_string = input_string

    def request(self, current_index, part):

        if current_index in self.__hash_list:
            return self.__hash_list[current_index]

        else:
            current_string = self._input_string + str(current_index)
            current_hash = hashlib.md5(
                current_string.encode('utf-8')).hexdigest()

            if part == 2:
                for _ in range(2016):
                    current_hash = hashlib.md5(
                        current_hash.encode('utf-8')).hexdigest()

            self.__hash_list[current_index] = current_hash

            return current_hash


input_string = input("Enter puzzle input: ")

# Part 1, 2.
for part in [1, 2]:

    hasher = Hasher(input_string)
    current_index = 0
    confirmed = []

    while True:

        new_hash = hasher.request(current_index, part)
        found_current = None

        for i in range(0, len(new_hash) - 2):
            if new_hash[i] == new_hash[i + 1] == new_hash[i + 2]:
                found_current = (new_hash, current_index, new_hash[i])
                break

        # Check the next 1000 hashes, worse performance than being able to check the
        # current 5-same hash against only candidates in the past 1000 hashes, but
        # that (the original approach) caused some dodgy ordering issue, and this
        # completes in a few minutes on my system, so probably alright.
        if found_current is not None:
            for j in range(1, 1001):

                test_hash = hasher.request(current_index + j, part)
                test_hash_confirmed = False

                for i in range(0, len(test_hash) - 4):
                    if found_current[2] == test_hash[i] == test_hash[i + 1] == test_hash[i + 2] == test_hash[i + 3] == test_hash[i + 4]:
                        confirmed.append((new_hash, found_current[1]))
                        test_hash_confirmed = True
                        break

                if test_hash_confirmed:
                    break

        if len(confirmed) >= 64:
            break

        current_index += 1

    print("Final answer for Part %d: %d" % (part, confirmed[63][1]))
