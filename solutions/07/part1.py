################################################################################
# Advent-of-Code 2023
# Day 07 Part 01
################################################################################

# import logging

# logging.basicConfig(
#     filename='part1.log',
#     level=logging.DEBUG)

# log = logging.getLogger()

from enum import Enum

#
#
#

class HandCombos(Enum):
    CRAP = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7
    
class Hand():

    def __init__(self, cards: str, bid: int):
        self.cards = [*cards]
        self.bid = bid
        self.combo = None
        self._calculate()

    def _calculate(self):
        
        # Run the numbers to see how many of each card we have in our hand.

        counts = {}
        for card in self.cards:
            if card in counts:
                counts[card] += 1
            else:
                counts[card] = 1

        # Now figure out what combo matches the current hand.

        if len(counts) == 1:
            self.combo = HandCombos.FIVE_OF_A_KIND
        elif len(counts) == 2:
            first_card_qty = counts[list(counts)[0]]
            if first_card_qty == 4 or first_card_qty == 1:
                self.combo = HandCombos.FOUR_OF_A_KIND
            else:
                self.combo = HandCombos.FULL_HOUSE
        else:
            if 3 in counts.values():
                self.combo = HandCombos.THREE_OF_A_KIND
            elif 2 in counts.values():
                if list(counts.values()).count(2) == 2:
                    self.combo = HandCombos.TWO_PAIR
                else:
                    self.combo = HandCombos.PAIR
            else:
                self.combo = HandCombos.CRAP

    def dump(self) -> str:
        return f'Hand: Cards:{self.cards}, Bid:{self.bid}, Combo:{self.combo}'


class Adjudicator():

    card_values = [*'23456789TJQKA']

    def __init__(self):
        self._hands = []

    def _decide_winner(self, challenger: Hand, defender: Hand) -> bool:

        # first, do the easy check. if the challenger's combo beats the
        # defender's combo they win. if the defender's combo is stronger,
        # they lose.

        if challenger.combo.value > defender.combo.value:
            return True
        elif challenger.combo.value < defender.combo.value:
            return False
        
        # from here on out, the combo's will be the same. so now we fall
        # back to the next method of deciding; high card

        for i in range(len(challenger.cards)):
            cha_value = self._get_card_value(challenger.cards[i])
            def_value = self._get_card_value(defender.cards[i])
            if cha_value == def_value:
                continue
            elif cha_value > def_value:
                return True
            elif cha_value < def_value:
                return False

    def _get_card_value(self, card: str) -> int:
        return self.card_values.index(card) + 1

    def dump(self) -> str:
        result = ''
        for i in range(len(self._hands)):
            result += f'{self._hands[i].dump()}\n'
        return result

    def get_final_score(self) -> int:
        result = 0
        for i in range(len(self._hands)):
            to_add = self._hands[i].bid * (i + 1)
            result += to_add
            print(f'{self._hands[i].dump()}: {self._hands[i].bid} * {i + 1} + {to_add} = {result}')
        return result

    def rank_hand(self, hand: Hand):

        # if this is the first hand, add it as the first hand in the list.

        if len(self._hands) == 0:
            self._hands.append(hand)
            return

        has_lost = False
        for i in range(len(self._hands)):
            winner = self._decide_winner(hand, self._hands[i])
            if winner:
                continue
            else:
                self._hands.insert(i, hand)
                has_lost = True
                break

        if not has_lost:
            self._hands.append(hand)

#
# MAIN
#

hands = []
with open('input.txt') as input_file:
    for input_line in input_file:
        hand_cards, hand_bid = input_line.strip().split()
        hands.append(Hand(hand_cards, int(hand_bid)))

mai = Adjudicator()

for i in range(0, len(hands)):
    mai.rank_hand(hands[i])

print(mai.get_final_score())

################################################################################
# END
################################################################################
