################################################################################
# Advent-of-Code 2023
# Day 05 Part 01
################################################################################

import logging
from enum import Enum
import re

logging.basicConfig(
    filename='part1.log',
    level=logging.DEBUG)

log = logging.getLogger()

#
#
#

class ConfigType(Enum):
    NONE = 0
    SEED2SOIL = 1
    SOIL2FERT = 2
    FERT2WATER = 3
    WATER2LIGHT = 4
    LIGHT2TEMP = 5
    TEMP2HUMID = 6
    HUMID2LOC = 7


class Sample():

    def __init__(self, type: ConfigType, src: int, dst: int, rng: int):
        self._type = type
        self._src = src
        self._dst = dst
        self._rng = rng
        self._src_min = src
        self._src_max = src + rng

    def get_mapping(self, src: int) -> int:
        log.debug('Checking for %d <= %d < %d', self._src_min, src, self._src_max)
        if src >= self._src_min and src < self._src_max:
            result = self._dst + (src - self._src)
            log.debug('%s: %d is within %d and %d, returning %d', self._type.name, src, self._src_min, self._src_max, result)
            return result
        else:
            return None

    def dump(self) -> str:
        return f'Sample({self._type}, {self._src}, {self._dst}, {self._rng})'

class Samples():

    def __init__(self):
        self._samples = {}
        for type in ConfigType:
            self._samples[type] = []

    def add_sample(self, type: ConfigType, src: int, dst: int, rng: int):
        self._samples[type].append(Sample(type, src, dst, rng))

    def dump(self) -> str:
        result = ''
        for type in self._samples:
            for sample in self._samples[type]:
                result += sample.dump()
        return result

    def get_samples(self, type: ConfigType) -> list:
        return self._samples[type]

class Mapping():

    def __init__(self, id):
        self._data = [id]

    def add_next(self, value: int):
        self._data.append(value)

    def get_location(self) -> int:
        return self._data[ConfigType.HUMID2LOC.value]

    def dump(self) -> str:
        result = f'SEED: {self._data[0]}'
        for i in range(1, len(self._data)):    
            result += f'\n{ConfigType(i).name}: {self._data[i]}'
        return result + '\n'
#
# MAIN
#

with open('input.txt') as input_file:
    input_data = input_file.readlines()

seeds = []
samples = Samples()

config_type = ConfigType.NONE
for row in input_data:
    data = row.strip()

    # if this is the seed list, store it and move on to the next line.

    if data.startswith('seeds:'):
        for value in re.finditer('\d+', data):
            seeds.append(value.group())
        continue

    # look for any lines that define the upcoming map to be processed.
    # once we identify which one, move on to the next line.

    match data:
        case 'seed-to-soil map:':
            config_type = ConfigType.SEED2SOIL
            continue
        case 'soil-to-fertilizer map:':
            config_type = ConfigType.SOIL2FERT
            continue
        case 'fertilizer-to-water map:':
            config_type = ConfigType.FERT2WATER
            continue
        case 'water-to-light map:':
            config_type = ConfigType.WATER2LIGHT
            continue
        case 'light-to-temperature map:':
            config_type = ConfigType.LIGHT2TEMP
            continue
        case 'temperature-to-humidity map:':
            config_type = ConfigType.TEMP2HUMID
            continue
        case 'humidity-to-location map:':
            config_type = ConfigType.HUMID2LOC
            continue

    # now that we know what we're processing, if the current line matches the
    # format we expect, grab the data and use it to load up our samples! Stuff
    # then into their associated lists in the main dict.

    if re.match('^\d+\s\d+\s\d+$', data):
        values = re.findall('\d+', data)
        samples.add_sample(config_type, int(values[1]), int(values[0]), int(values[2]))

# now that we have all the data, it's time to compute!

seed_paths = []
for seed in seeds:
    seed_id = int(seed)
    seed_path = Mapping(seed_id)

    seek_id = seed_id

    log.debug('Seeking ID: %d', seek_id)

    for i in range(ConfigType.HUMID2LOC.value):

        log.debug('processing for %s', ConfigType(i+1).name)

        not_found = True
        for sample in samples.get_samples(ConfigType(i+1)):
            print(sample)
            mapping_result = sample.get_mapping(seek_id)
            log.debug('mapping result %s for id %d from %s', mapping_result, seek_id, sample.dump())
            if mapping_result:
                seed_path.add_next(mapping_result)
                seek_id = mapping_result
                not_found = False
                break

        if not_found:
            seed_path.add_next(seek_id)

    seed_paths.append(seed_path)

how_low_can_we_go = 99999999999999999999
for foo in seed_paths:
    print(foo.dump())
    foo_location = foo.get_location()
    if foo_location < how_low_can_we_go:
        how_low_can_we_go = foo_location

print(how_low_can_we_go)

################################################################################
# END
################################################################################
