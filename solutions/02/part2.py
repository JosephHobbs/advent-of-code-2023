################################################################################
# Advent-of-Code 2023
# Day 02 Part 02
################################################################################

import logging
import re

logging.basicConfig(
    filename='AoC_D02P02.log',
    level=logging.DEBUG)

log = logging.getLogger()

#
#
#

class GameResult:

    def __init__(self, id: int):
        self.id = id
        self.red_max = 0
        self.red_min = 99
        self.green_max = 0
        self.green_min = 99
        self.blue_max = 0
        self.blue_min = 99

    def add_sample(self, sample: str):
        cube_count, cube_color = sample.split(' ', 1)
        cube_count = int(cube_count)

        if cube_color == 'red' and cube_count > self.red_max:
            self.red_max = cube_count
        elif cube_color == 'green' and cube_count > self.green_max:
            self.green_max = cube_count
        elif cube_color == 'blue' and cube_count > self.blue_max:
            self.blue_max = cube_count

        if cube_color == 'red' and cube_count < self.red_min:
            self.red_min = cube_count
        elif cube_color == 'green' and cube_count < self.green_min:
            self.green_min = cube_count
        elif cube_color == 'blue' and cube_count < self.blue_min:
            self.blue_min = cube_count


#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

games = []

for game in input_data:

    # break it up into the 2 parts we need...
    prefix, the_rest = game.split(':',1)

    # figure out the game ID.  We're doing this the lazy way given they always
    # start with the same 5 characters: 'Game '.
    game_id = prefix.strip()[5:]

    # Split the rest on delims , or ; so we can get the various item counts.
    cube_count_samples = re.split('[\;|\,]\s', the_rest.strip())

    # Generate Game Result and add it to our list of games.
    new_game = GameResult(game_id)
    for sample in cube_count_samples:
        new_game.add_sample(sample)

    games.append(new_game)

tally = 0
for game in games:
    # print(f'{game.id} => {game.red_min} : {game.green_min} : {game.blue_min}')
    power = game.red_max * game.green_max * game.blue_max
    print(f'{game.id} => {game.red_max} x {game.green_max} x {game.blue_max} = {power}')
    tally += power

print(tally)

################################################################################
# END
################################################################################
