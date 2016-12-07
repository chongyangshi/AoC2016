###################################
# Such seven                      #
#                 Many splits     #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

from collections import OrderedDict


def ABBA_checker(strin):

    has_ABBA = False
    for i in range(0, len(strin) - 3):
        if strin[i] == strin[i + 3] and strin[i + 1] == strin[i + 2] and strin[i] != strin[i + 1]:
            has_ABBA = True
            break

    return has_ABBA


def ABA_checker(strin):

    has_ABA = False
    ABAs = []
    for i in range(0, len(strin) - 2):
        if strin[i] == strin[i + 2] and strin[i] != strin[i + 1]:
            has_ABA = True
            ABAs.append(strin[i:i + 3])

    return has_ABA, ABAs


def BAB_checker(strin, ABAs):

    has_BAB = False
    for i in range(0, len(strin) - 2):
        for ABA in ABAs:
            if strin[i] == ABA[1] and strin[i + 1] == ABA[0] and strin[i + 2] == ABA[1]:
                has_BAB = True
                break
        if has_BAB:
            break

    return has_BAB


with open("inputs/day7-1.txt") as f:
    content = f.readlines()

lines = map(str.strip, content)
TLS_lines = 0
SSL_lines = 0
for line in lines:

    # Properly split the line down.
    processed_line = []
    line_split = line.split('[')
    for item in line_split:
        if ']' in item:
            result = item.split(']')
        else:
            result = [item]
        processed_line += result

    # Rotate between outside and inside brackets to check things.
    # Part 1
    outside = True
    valid1 = True
    outside_has_ABBA = False
    for part in processed_line:
        if outside == True:
            outside = False
            if ABBA_checker(part):
                outside_has_ABBA = True
        else:
            outside = True
            if ABBA_checker(part):
                valid1 = False
                break

    # Part 2
    outside = True
    ABAs = []
    for part in processed_line:
        if outside == True:
            outside = False
            ABA_T, ABA_s = ABA_checker(part)
            if ABA_T:
                ABAs += ABA_s
        else:
            outside = True

    # Need to walk through parts again to check for all matchings.
    outside = True
    valid2 = False
    if ABAs != []:
        for part in processed_line:
            if outside == True:
                outside = False
            else:
                outside = True
                if BAB_checker(part, ABAs):
                    valid2 = True

    # Tallying.
    if valid1 and outside_has_ABBA:
        TLS_lines += 1

    if valid2:
        SSL_lines += 1

print("Final answer for Part 1: %s" % (TLS_lines))
print("Final answer for Part 2: %s" % (SSL_lines))
