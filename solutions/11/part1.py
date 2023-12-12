################################################################################
# Advent-of-Code 2023
# Day 11 Part 02
################################################################################

#
#
#

class Galaxy():

    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.coord_x = x
        self.coord_y = y


class StarMap():

    SPACE = '.'
    STAR = '#'

    def __init__(self, data: list):
        self._data = data
        self.galaxies = []
        self._find_galaxies()

    def _find_galaxies(self):
        for y in range(len(self._data)):
            for x in range(len(self._data[y])):
                if self._data[y][x] == StarMap.STAR:
                    self.galaxies.append(Galaxy(len(self.galaxies), x, y))

    def get_distance(self, source: int, destination: int) -> int:
        dist_x = abs(self.galaxies[destination].coord_x - self.galaxies[source].coord_x)
        dist_y = abs(self.galaxies[destination].coord_y - self.galaxies[source].coord_y)
        return (dist_x + dist_y)


class Cartographer():

    def generate_star_map(data: list) -> StarMap:
        
        star_map_data = []

        # Figure out which columns contain at least one galaxy and record
        # that information. We need this info to account for galactic
        # expansion.

        col_has_galaxy = [False] * len(data[0])
        for row in data:
            for idx in range(len(row)):
                if row[idx] == StarMap.STAR:
                    col_has_galaxy[idx] = True

        # Run through the inputs again and build our final star map. In this
        # case we're going to transfer the map cell by cell. If we hit a
        # column with no galaxy at all, add another space for expansion. Once
        # a row is created, check to see if it has any galaxies in it. If none
        # are present, duplicate the row entirely for expansion as well.

        for row in data:
            star_map_data.append([])
            for idx in range(len(row)):
                star_map_data[-1].append(row[idx])
                if not col_has_galaxy[idx]:
                    star_map_data[-1].append(StarMap.SPACE)
            if StarMap.STAR not in star_map_data[-1]:
                star_map_data.append(star_map_data[-1])

        return StarMap(star_map_data)

#
# MAIN
#

# Read in our input file, clean up each row data and store it as a list.

input_data = []
with open('input.txt') as input_file:
    for input_row in input_file:
        input_data.append(list(input_row.strip()))

# Generate a StarMap using the input data. Then use that data to calculate
# each galaxy's distance and sum them all together.

star_map = Cartographer.generate_star_map(input_data)

total_galaxies = len(star_map.galaxies)
total_distance = 0
for i in range(total_galaxies):
    if i != (total_galaxies - 1):
        for j in range(i + 1, total_galaxies):
            total_distance += star_map.get_distance(i, j)

print(total_distance)

################################################################################
# END
################################################################################
