################################################################################
# Advent-of-Code 2023
# Day 06 Part 01
################################################################################

import re

#
#
#

class Race():

    def __init__(self, time: int, distance: int):
        self._time = time
        self._distance = distance

    def get_record_breaker_count(self) -> int:

        result = 0
        for i in range(2, self._time):
            button_time = i
            travel_time = self._time - button_time
            travel_distance = button_time * travel_time

            if travel_distance > self._distance:
                result += 1

        return result

    def dump(self) -> str:
        return f'Race: t = {self._time}, d = {self._distance}'

#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

time_values = re.findall('\d+', input_data[0])
dist_values = re.findall('\d+', input_data[1])

races = []
for i in range(len(time_values)):
    races.append(Race(int(time_values[i]), int(dist_values[i])))

final_tally = 1
for race in races:
    final_tally *= race.get_record_breaker_count()

print(final_tally)

################################################################################
# END
################################################################################
