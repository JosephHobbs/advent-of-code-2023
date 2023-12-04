################################################################################
# Advent-of-Code 2023
# Day 04 Part 01
################################################################################

import logging
import re

logging.basicConfig(
    filename='part1.log',
    level=logging.DEBUG)

log = logging.getLogger()

#
# Classes
#

class ScratchCard():

    def __init__(self, id: int):
        self.id = id
        self._winning_numbers = []
        self._player_numbers = []

    def add_winning_number(self, number: int):
        self._winning_numbers.append(number)

    def add_player_number(self, number: int):
        self._player_numbers.append(number)

    def get_value(self) -> int:
        winners = 0
        for number in self._player_numbers:
            if number in self._winning_numbers:
                winners += 1

        if winners <= 1:
            return winners
        else:
            return (1 * 2 ** (winners - 1))

    def dump(self) -> str:
        return f'Scratch Card >>>\nID: {self.id}\nWinning Numbers: {self._winning_numbers}\nPlayer Numbers: {self._player_numbers}\nValue: {self.get_value()}'

#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

cards = {}

for card in input_data:

    for card_data in re.finditer('^Card\s+(\d+)\:\s([\d\s]+)\s\|\s([\d\s]+)$', card.strip()):
        new_card = ScratchCard(card_data.group(1))

        for number in re.finditer('\d+', card_data.group(2)):
            new_card.add_winning_number(int(number.group()))

        for number in re.finditer('\d+', card_data.group(3)):
            new_card.add_player_number(int(number.group()))

        cards[new_card.id] = new_card


total_points = 0
for card_id in cards:
    # print(cards[card_id].dump())
    total_points += cards[card_id].get_value()

print(total_points)

################################################################################
# END
################################################################################
