################################################################################
# Advent-of-Code 2023
# Day 01 Part 02
################################################################################

import logging
import re

logging.basicConfig(filename='part2.log', level=logging.INFO)

log = logging.getLogger('aoc2023.01')

# replacements = {
#     'one': '1',
#     'two': '2',
#     'three':'3',
#     'four':'4',
#     'five':'5',
#     'six':'6',
#     'seven':'7',
#     'eight':'8',
#     'nine':'9'
# }

replacements = {
    'one': 'o1ne',
    'two': 't2wo',
    'three':'t3hree',
    'four':'f4our',
    'five':'f5ive',
    'six':'s6ix',
    'seven':'s7even',
    'eight':'e8ight',
    'nine':'n9ine'
}

def word_to_num(data_in: str) -> str:

    # result = data_in
    # for key in replacements:
    #     result = re.sub(key, replacements[key], result)
    # return result

    # BRUH, did all this @#$% below to ensure I was replacing in the correct
    # order for those oneight scenarios just to find out that should be 18
    # and not 1ight...  Using the replacements hack above, the block above
    # worked just as well.  BOOOOOO

    log.debug('processing input %s', data_in)

    data = data_in

    while True:
 
        start_over = False

        for pos in range(0, len(data)):
            sub_data = data[pos:]
            for key in replacements:
                log.debug('checking to see if %s starts with %s', sub_data, key)
                if sub_data.startswith(key):
                    data = re.sub(key, replacements[key], data, 1)
                    log.debug('data is now %s', data)
                    start_over = True
                if start_over:
                    break
            if start_over:
                break

        if not start_over:
            log.debug('returning %s; was %s', data, data_in)
            return data

# Main


with open('input.txt') as input_file:
    input_data = input_file.readlines()

total = 0

for record in input_data:
    log.info('starting with input %s', record.strip())
    new_record = word_to_num(record.strip())
    log.info('looking for digits in %s', new_record)
    digits = re.findall('\d', new_record)
    log.info('found digits: %s', digits)
    total += int(f'{digits[0]}{digits[-1]}')
    log.info(f'Adding {digits[0]}{digits[-1]} to Total: {total}')

print(total)
    
################################################################################
# END
################################################################################
