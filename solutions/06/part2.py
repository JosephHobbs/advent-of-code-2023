################################################################################
# Advent-of-Code 2023
# Day 06 Part 02
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

total_time = ''
total_distance = ''
for i in range(len(time_values)):
    total_time += time_values[i]
    total_distance += dist_values[i]

race = Race(int(total_time), int(total_distance))

print(race.get_record_breaker_count())

################################################################################
# END
################################################################################
