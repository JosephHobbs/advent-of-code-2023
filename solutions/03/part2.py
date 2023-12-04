################################################################################
# Advent-of-Code 2023
# Day 03 Part 02
################################################################################

import logging
import re

logging.basicConfig(
    filename='AoC_D03P02.log',
    level=logging.DEBUG)

log = logging.getLogger()

#
# Classes
#

class Sample():

    def __init__(self, start_pos: int, end_pos: int, value: int):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.value = value


class Samples():

    def __init__(self):
        self._samples = {}
        self._current_row = -1

    def add_row(self, row: str):

        self._current_row += 1

        for value in re.finditer('\d+', row):
            new_sample = Sample(value.start(), value.end(), value.group())
            for pos in range(value.start(), value.end()):
                coord = f'{self._current_row}:{pos}'
                self._samples[coord] = new_sample

    def seek_gears(self, x: int, y: int) -> int:

        log.debug('checking for gears around %d:%d...', x, y)

        parts = []
        for r in range(x - 1, x + 2):
            for c in range (y - 1, y + 2):
                target = f'{c}:{r}'
                log.debug('checking for part in position %s...', target)
                if target in self._samples:
                    if self._samples[target] not in parts:
                        log.debug('adding part %s to list!', self._samples[target].value)
                        parts.append(self._samples[target])
                    else:
                        log.debug('part already in list, skipping...')

        if len(parts) == 2:
            log.debug('found gear with 2 part numbers...')
            ratio = int(parts[0].value) * int(parts[1].value)
            return ratio
        
        log.debug('not a gear, returning empty list.')
        return 0

#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

samples = Samples()
for row in input_data:
    samples.add_row(row.strip())

tally = 0
current_row = -1
for row in input_data:
    current_row += 1
    for value in re.finditer('\*', row.strip()):
        ratio = samples.seek_gears(value.start(), current_row)
        tally += ratio

print(tally)

################################################################################
# END
################################################################################
