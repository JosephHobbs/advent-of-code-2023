################################################################################
# Advent-of-Code 2023
# Day 08 Part 01
#
# LLRRRLLRRRLRRRLR
#
# BQV = (HFG, GDR)
#
################################################################################

import re

#
#
#

class Node():

    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def move(self, direction: str) -> str:
        if direction == 'L':
            return self.left
        elif direction == 'R':
            return self.right
        return None

    def dump(self) -> str:
        return f'Node({self.name} - L:{self.left}, R:{self.right})'

#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

# Read in all of our instructions and store them as separate elements
# in a list.

instructions = []
for instruction in re.findall('[LR]{1}', input_data[0]):
    instructions.append(instruction)

# Read in all nodes and their associated references. Initialize a Node
# for each entry and add them to the dict of nodes. Store by node name
# so we can find them easier later on...

nodes = {}
for line_number in range(1, len(input_data)):
    input_line = input_data[line_number].strip()

    if not input_line:
        continue

    node_data = re.search('^(?P<node_name>[A-Z]{3}) \= \((?P<to_left>[A-Z]{3}), (?P<to_right>[A-Z]{3})\)$', input_line)
    new_node = Node(node_data.group('node_name'), node_data.group('to_left'), node_data.group('to_right'))

    nodes[new_node.name] = new_node

# Now that we have all of our data, it's time to follow the network and
# see what we can find.

current_position = 'AAA'
steps_taken = 0

not_at_zzz = True
while not_at_zzz == True:
    for instruction in instructions:

        print(f'starting at {current_position}...')
        current_node = nodes[current_position]
        print(f'moving {instruction}...')
        current_position = current_node.move(instruction)
        print(f'now at {current_position}!')
        steps_taken += 1

        if current_position == 'ZZZ':
            not_at_zzz = False
            break

print(f'it took {steps_taken} steps!')

################################################################################
# END
################################################################################
