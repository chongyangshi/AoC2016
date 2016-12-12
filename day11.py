###################################
# Such eleven                     #
#                  Much time      #
#       Very Doge                 #
###################################
# By icydoge <icydoge@gmail.com>  #
###################################

import itertools

FLOORS = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
DESTINATION = FLOORS['fourth']

def elevator_destinations(elevator):
    if elevator <= 1:
        return [2]
    elif elevator >= DESTINATION:
        return [3]
    else:
        return [elevator - 1, elevator + 1]

def find_path(steps, max_steps, elevator, floors_content):

    if steps >= max_steps:
        return None

    current_content = floors_content[elevator]

    current_RTGs = [i for i in current_content if not i.endswith('-compatible')]
    current_chips = [i.split('-')[0] for i in current_content if i.endswith('-compatible')]

    for chip in current_chips:
        if (chip not in current_RTGs) and (len(current_RTGs) > 0): 
            return None

    if (elevator == DESTINATION) and (len(current_content) >= total):
        print("Success: %d" % (steps))
        return steps

    possible_takes = list(itertools.combinations(current_content, 2)) + list(itertools.combinations(current_content, 1)) + [()]
    possible_actions = list(itertools.product(possible_takes, elevator_destinations(elevator)))

    results = []
    for action in possible_actions:

        new_content = {i:floors_content[i][:] for i in floors_content}

        for item in action[0]:
            new_content[action[1]].append(item)
            new_content[elevator].remove(item)

        new_RTGs = [i for i in new_content[elevator] if not i.endswith('-compatible')]
        new_chips = [i.split('-')[0] for i in new_content[elevator] if i.endswith('-compatible')]

        new_content_works = True
        for chip in new_chips:
            if (chip not in new_RTGs) and (len(new_RTGs) > 0): 
                new_content_works = False
                break

        if new_content_works:
            results.append(find_path(steps + 1, max_steps, action[1], new_content))
            print(steps, action, end='\r')
        else:
            pass

    min_steps = [i for i in results if i is not None]

    if len(min_steps) > 0:
        return min(min_steps)
    else:
        return None

with open("inputs/day11-1.txt") as f:
    content = f.readlines()

lines = list(map(str.strip, content))
floors_content = {FLOORS[i]: [] for i in FLOORS}
total = 0

for line in lines:

    line_split = line[:-1].split(', ')
    floor = line_split[0].split(' ')[1]
    for s in line_split:
        line_split2 = s.split(' ')
        
        if "generator" in s:
            floors_content[FLOORS[floor]].append(line_split2[line_split2.index("generator") - 1])
            total += 1
        elif "microchip" in s:
            floors_content[FLOORS[floor]].append(line_split2[line_split2.index("microchip") - 1])
            total += 1

steps = 0
elevator = 1
max_steps = 100
part_one_answer = find_path(steps, max_steps, elevator, floors_content)
print('', end='\r\n')
print(part_one_answer)



