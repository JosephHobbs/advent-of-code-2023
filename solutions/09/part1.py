################################################################################
# Advent-of-Code 2023
# Day 09 Part 01
#
#   3 10 23 46 99 234
#
#   2174807984: too high
#
################################################################################

# import logging

# logging.basicConfig(
#     filename='part1.log',
#     level=logging.DEBUG)

# log = logging.getLogger()

#
#
#

class History():

    def __init__(self, samples: list):
        
        # prepare internal storage spaces and then initialize any required
        # items in prep for processing.

        self._samples = []
        self._last_digits = []

        self._samples.append([])
        self._samples[0] = samples

        # run calculations to predict the next value...

        self._calculate()

    def _calculate(self) -> int:

        # prepare a location to store our final digits and start
        # extrapolating out the data we have.

        self._extrapolate()

        # prepare our last digits storage. then go bottom up and figure
        # out what the last digit for each row.

        for _ in range(len(self._samples)):
            self._last_digits.append(0)

        for i in range(len(self._samples) - 2, -1, -1):
            self._last_digits[i] = self._samples[i][-1] + self._last_digits[i + 1]

    def _extrapolate(self):

        # prepare the next line for extrapolation and figure out the
        # id of our current (new) and previous (data here) group.

        self._samples.append([])
        cur_id = len(self._samples) - 1
        pre_id = cur_id - 1

        # loop through and calculate the difference of each number
        # pair in the PRE list. Store the result in the CUR list.

        for i in range(1, len(self._samples[pre_id])):
            self._samples[cur_id].append(
                self._samples[pre_id][i] - self._samples[pre_id][i - 1])
        
        # add up all the values in the CUR list. If the answer is
        # ZERO, we've reached the bottom. If not, do it again!

        for num in self._samples[cur_id]:
            if num != 0:
                self._extrapolate()
                break

    def get_predicted_value(self) -> int:
        return self._last_digits[0]

    def dump(self) -> str:

        result = ''
        for i in range(len(self._samples)):
            result += f'{i}:'
            for value in self._samples[i]:
                result += f' {value}'
            result += f' [{self._last_digits[i]}]\n'

        return result


#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

# Parse and initialize our History objects.

data = []
for line_of_history in input_data:
    history = History([int(i) for i in line_of_history.strip().split()])
    # log.debug('%s', history.dump())
    data.append(history.get_predicted_value())

print(f'{sum(data)}')

################################################################################
# END
################################################################################
