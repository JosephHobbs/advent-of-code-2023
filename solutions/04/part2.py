################################################################################
# Advent-of-Code 2023
# Day 04 Part 02
################################################################################

import logging
import re

logging.basicConfig(
    filename='part2.log',
    level=logging.DEBUG)

log = logging.getLogger()

#
# Classes
#

class ScratchCard():

    def __init__(self, id: int):
        self.id = int(id)
        self._winning_numbers = []
        self._player_numbers = []

    def add_winning_number(self, number: int):
        self._winning_numbers.append(number)

    def add_player_number(self, number: int):
        self._player_numbers.append(number)

    def get_winning_cards(self) -> list:
        winners = 0
        for number in self._player_numbers:
            if number in self._winning_numbers:
                winners += 1

        winning_cards = []

        if winners:
            first_card_id = self.id + 1
            for card_id in range(first_card_id, first_card_id + winners):
                use_card_id = card_id
                if use_card_id > 199:
                    use_card_id -= 199
                winning_cards.append(card_id)

        return winning_cards

    def dump(self) -> str:
        return f'Scratch Card >>>\nID: {self.id}\nWinning Numbers: {self._winning_numbers}\nPlayer Numbers: {self._player_numbers}\nWinning Cards: {self.get_winning_cards()}'

#
# Functions
#

def count_cards(card_id: int, original_set: dict) -> int:

    counter = 1

    winning_card_ids = original_set[card_id].get_winning_cards()
    if winning_card_ids:
        for winning_card_id in winning_card_ids:
            counter += count_cards(winning_card_id, original_set)

    return counter

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


total_cards = 0
for card_id in cards:
    total_cards += count_cards(card_id, cards)

print(total_cards)

################################################################################
# END
################################################################################
