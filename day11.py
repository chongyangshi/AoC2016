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
        print(DESTINATION)
        return [DESTINATION - 1]
    else:
        return [elevator - 1, elevator + 1]

def find_path(steps, max_steps, elevator, floors_content, total, states_seen):

    new_states = [i[:] for i in states_seen]

    # Exceed maximum iteration, stop.
    if steps >= max_steps:
        return None

    current_content = floors_content[elevator]

    # Done moving, return.
    if (elevator == DESTINATION) and (len(current_content) >= total):
        print("Success at %d" % (steps))
        return steps

    # No backtracking down to fully empty floors.
    minimum_floor_with_item = 0
    for i in range(1, DESTINATION + 1):
        if len(floors_content[i]) == 0:
            minimum_floor_with_item = i + 1
        else:
            break

    # Build current floor inventory and possible combinations.
    current_RTGs = [i for i in current_content if not i.endswith('-compatible')]
    current_chips = [i.split('-')[0] for i in current_content if i.endswith('-compatible')]
    possible_takes = list(itertools.combinations(current_content, 2)) + list(itertools.combinations(current_content, 1))
    possible_actions = list(itertools.product(possible_takes, elevator_destinations(elevator)))

    
    results = []

    # Build current dict of RTG locations.
    RTG_floors = {}
    for f in range(1, DESTINATION + 1):
        for i in floors_content[f]:
            if not i.endswith('-compatible'):
                RTG_floors[i] = f

    chip_floors = {}
    for f in range(1, DESTINATION + 1):
        for i in floors_content[f]:
            if i.endswith('-compatible'):
                chip_floors[i.split('-')[0]] = f

    # Build and check states seen.
    state = []
    for floor in floors_content:

        floor_RTGs = [i for i in floors_content[floor] if not i.endswith('-compatible')]
        floor_chips = [i.split('-')[0] for i in floors_content[floor] if i.endswith('-compatible')]

        for chip in floor_chips:
            state.append((floor, RTG_floors[chip]))

    state = sorted(state)

    #state = []
    #for f in range(1, DESTINATION + 1):
    #    for i in floors_content[f]:
    #        state.append((i, f))

    #state = sorted(state)


    if state in new_states:
        return None
    else:
        new_states.append(state)

    two_up_possible = False
    two_down_possible = False

    for action in possible_actions:
        
        # Not moving down to cleared floors.
        if action[1] < minimum_floor_with_item:
            continue

        # Always try to bring the max amount of items up or down.
        #if two_up_possible and (action[1] > elevator) and (len(action[0]) == 1):
        #    continue

        #if two_down_possible and (action[1] < elevator) and (len(action[0]) == 1):
        #    continue 

        new_content = {i:floors_content[i][:] for i in floors_content}

        for item in action[0]:
            new_content[action[1]].append(item)
            new_content[elevator].remove(item)

        new_content_works = True

        for floor in new_content:

            new_RTGs = [i for i in new_content[floor] if not i.endswith('-compatible')]
            new_chips = [i.split('-')[0] for i in new_content[floor] if i.endswith('-compatible')]
            
            for chip in new_chips:
                if (chip not in new_RTGs) and (len(new_RTGs) > 0): 
                    new_content_works = False

        if new_content_works and (len(action[0]) == 2) and (action[1] > elevator):
            two_up_possible = True

        elif new_content_works and (len(action[0]) == 2) and (action[1] < elevator):
            two_down_possible = True

        if new_content_works:
            results.append(find_path(steps + 1, max_steps, action[1], new_content, total, new_states))
            #print("Progress: ", steps, action, end='\r')
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
        generator_locations = [i for i in range(len(line_split2)) if 'generator' in line_split2[i]]
        microchip_locations = [i for i in range(len(line_split2)) if 'microchip' in line_split2[i]]
        total += len(generator_locations) + len(microchip_locations)
        floors_content[FLOORS[floor]] += [line_split2[i - 1] for i in generator_locations]
        floors_content[FLOORS[floor]] += [line_split2[i - 1] for i in microchip_locations]

steps = 0
elevator = 1
max_steps = 100
states_seen = []
part_one_answer = find_path(steps, max_steps, elevator, floors_content, total, states_seen)
print('', end='\r\n')
print(part_one_answer)



