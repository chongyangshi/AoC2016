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
    ''' Helper function to return possible elevator destinations. '''

    if elevator <= 1:
        return [2]
    elif elevator >= DESTINATION:
        return [DESTINATION - 1]
    else:
        return [elevator - 1, elevator + 1]


def check_safety(floors_content):
    ''' Returns True if the current item placement state is safe, False otherwise. '''

    safe = True

    for floor in floors_content:

        floor_RTGs = [i for i in floors_content[
            floor] if not i.endswith('-compatible')]
        floor_chips = [
            i.split('-')[0] for i in floors_content[floor] if i.endswith('-compatible')]

        for chip in floor_chips:
            if (chip not in floor_RTGs) and (len(floor_RTGs) > 0):
                safe = False
                break

        if not safe:
            break

    return safe


def build_state(floors_content, elevator):
    ''' Build a list of equivalent states for item placements, it is very important that
        the location of the elevator form part of the state. '''

    RTG_floors = {}
    for f in range(1, DESTINATION + 1):
        for i in floors_content[f]:
            if not i.endswith('-compatible'):
                RTG_floors[i] = f

    state = []
    for floor in floors_content:

        floor_RTGs = [i for i in floors_content[
            floor] if not i.endswith('-compatible')]
        floor_chips = [
            i.split('-')[0] for i in floors_content[floor] if i.endswith('-compatible')]

        for chip in floor_chips:
            state.append((floor, RTG_floors[chip]))

    state = sorted(state)

    return (state, elevator)


def process_input(content):
    ''' Parsing input, in a function due to the nature of this question. '''

    lines = list(map(str.strip, content))
    floors_content = {FLOORS[i]: [] for i in FLOORS}
    total = 0

    for line in lines:

        line_split = line[:-1].split(', ')
        floor = line_split[0].split(' ')[1]

        for s in line_split:
            line_split2 = s.split(' ')
            generator_locations = [i for i in range(
                len(line_split2)) if 'generator' in line_split2[i]]
            microchip_locations = [i for i in range(
                len(line_split2)) if 'microchip' in line_split2[i]]
            total += len(generator_locations) + len(microchip_locations)
            floors_content[FLOORS[floor]] += [line_split2[i - 1]
                                              for i in generator_locations]
            floors_content[FLOORS[floor]] += [line_split2[i - 1]
                                              for i in microchip_locations]

    return floors_content, total


def BFS_find(floors_content, final_total, question_part):
    ''' Dirty BFS work. '''

    # Queue item: content, new elevator position, steps
    check_queue = [(floors_content, 1, 0)]
    steps = 0
    states_seen = []
    while len(check_queue) > 0:

        current_search = check_queue[0]
        check_queue = check_queue[1:]

        elevator = current_search[1]
        steps = current_search[2]
        current_content = {i: current_search[
            0][i][:] for i in current_search[0]}

        # Success, break and report.
        if (elevator == DESTINATION) and (len(current_content[DESTINATION]) == final_total):
            print("Final answer for Part %d: %d" % (question_part, steps))
            break

        # Otherwise, if current state still safe, continue to check.
        if check_safety(current_content):

            # No backtracking down to fully empty floors.
            # Get minimum non-backtracking destination.
            minimum_floor_with_item = 0
            for i in range(1, DESTINATION + 1):
                if len(current_content[i]) == 0:
                    minimum_floor_with_item = i + 1
                else:
                    break

            # Build current floor inventory and possible combinations.
            current_level_content = current_content[elevator]
            current_RTGs = [
                i for i in current_level_content if not i.endswith('-compatible')]
            current_chips = [
                i.split('-')[0] for i in current_level_content if i.endswith('-compatible')]
            possible_takes = list(itertools.combinations(
                current_level_content, 2)) + list(itertools.combinations(current_level_content, 1))
            possible_actions = list(itertools.product(
                possible_takes, elevator_destinations(elevator)))

            # Add new nodes to search.
            for action in possible_actions:

                # No floor backtracking.
                if action[1] < minimum_floor_with_item:
                    continue

                new_content = {i: current_content[i][:]
                               for i in current_content}

                for item in action[0]:
                    new_content[action[1]].append(item)
                    new_content[elevator].remove(item)

                # Check for repeated states.
                state = build_state(new_content, action[1])
                if state in states_seen:
                    continue
                else:
                    states_seen.append(state)

                check_queue.append((new_content, action[1], steps + 1))


# Part 1, 2 from separate input files.
part = 1
for input_file in ["inputs/day11-1.txt", "inputs/day11-2.txt"]:
    with open(input_file) as f:
        content = f.readlines()
        initial_state, total = process_input(content)
        BFS_find(initial_state, total, part)
        part += 1
