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


class VoidTracker():

    def __init__(self):
        self.voids_x = []
        self.voids_y = []

    def add_x(self, col: int):
        self.voids_x.append(col)

    def add_y(self, row: int):
        self.voids_y.append(row)


class StarMap():

    SPACE = '.'
    STAR = '#'
    VOID_SIZE = 1000000

    def __init__(self, data: list, voids: VoidTracker):
        self._data = data
        self.galaxies = []
        self._voids = voids
        self._find_galaxies()

    def _find_galaxies(self):
        for y in range(len(self._data)):
            for x in range(len(self._data[y])):
                if self._data[y][x] == StarMap.STAR:
                    self.galaxies.append(Galaxy(len(self.galaxies), x, y))

    def _expand(self, src: int, dst: int, void_locations):
        total_voids = 0
        for void in void_locations:
            if (src < void and dst > void) or (src > void and dst < void):
                total_voids += 1
        
        return abs(src - dst) + (total_voids * (StarMap.VOID_SIZE - 1))


    def get_distance(self, source: int, destination: int) -> int:
        dist_x = self._expand(
            self.galaxies[source].coord_x,
            self.galaxies[destination].coord_x,
            self._voids.voids_x)

        dist_y = self._expand(
            self.galaxies[source].coord_y,
            self.galaxies[destination].coord_y,
            self._voids.voids_y)

        return (dist_x + dist_y)


class Cartographer():

    def generate_star_map(data: list) -> StarMap:
        
        star_map_data = []
        void_tracker = VoidTracker()

        # Figure out which columns contain at least one galaxy and record
        # that information. We need this info to account for galactic
        # expansion.

        col_has_galaxy = [False] * len(data[0])
        for row in data:
            for idx in range(len(row)):
                if row[idx] == StarMap.STAR:
                    col_has_galaxy[idx] = True

        for i in range(len(col_has_galaxy)):
            if not col_has_galaxy[i]:
                void_tracker.add_x(i)

        # Run through the inputs again and build our final star map. In this
        # case we're going to transfer the map cell by cell. If we hit a
        # column with no galaxy at all, add another space for expansion. Once
        # a row is created, check to see if it has any galaxies in it. If none
        # are present, duplicate the row entirely for expansion as well.

        for row in data:
            star_map_data.append([])
            for idx in range(len(row)):
                star_map_data[-1].append(row[idx])
            if StarMap.STAR not in star_map_data[-1]:
                void_tracker.add_y(len(star_map_data) - 1)

        return StarMap(star_map_data, void_tracker)

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
