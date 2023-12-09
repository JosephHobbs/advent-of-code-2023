################################################################################
# Advent-of-Code 2023
# Day 08 Part 02
#
# LLRRRLLRRRLRRRLR
#
# BQV = (HFG, GDR)
#
################################################################################

import re
import math

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

class Path():

    def __init__(self, start_pos: str):
        self.current_position = start_pos
        self.total_steps = 0

    def is_at_end(self) -> bool:
        return self.current_position.endswith('Z')

    def move_to(self, next_pos: str):
        self.current_position = next_pos
        self.total_steps += 1

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

# Determine our starting position(s)...

paths = []

for node in nodes:
    if nodes[node].name.endswith('A'):
        paths.append(Path(nodes[node].name))

# Process each path for one full cycle, keeping track of how many
# steps each one required...

not_at_zzz = True
while not_at_zzz == True:
    for instruction in instructions:
        for path in paths:
            if not path.is_at_end():
                current_node = nodes[path.current_position]
                path.move_to(current_node.move(instruction))

        # if all of our paths have reached the end, set a flag so we
        # can break out!

        finished = True
        for path in paths:
            if not path.is_at_end():
                finished = False

        if finished:
            not_at_zzz = False
            break

# Use all of our step counts to calculate the Least Common Multiple. This
# is the result we are after!

step_counts = []
for path in paths:
    step_counts.append(path.total_steps)

print(math.lcm(*step_counts))

################################################################################
# END
################################################################################
