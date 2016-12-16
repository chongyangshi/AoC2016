###################################
# Such lives                      #
#                  Much craze     #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

REQUIRED_LENGTHS = [272, 35651584]

current_string = input("Enter your puzzle input: ")

for length in REQUIRED_LENGTHS:

    while len(current_string) < length:
        reversed_current = ''.join([str((int(i) + 1) % 2)
                                    for i in list(reversed(current_string))])
        current_string = current_string + '0' + reversed_current

    full_string = current_string[:length]

    while True:
        current_checksum = ""
        for i in range(0, len(full_string), 2):
            if full_string[i] == full_string[i + 1]:
                current_checksum += '1'
            else:
                current_checksum += '0'

        if len(current_checksum) % 2 != 0:
            break
        else:
            full_string = current_checksum

    print("Final answer for Part %d: %s" %
          (REQUIRED_LENGTHS.index(length) + 1, current_checksum))
