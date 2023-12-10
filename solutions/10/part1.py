################################################################################
# Advent-of-Code 2023
# Day 10 Part 01
################################################################################

#
#
#

class Pipe():

    BOTTOM =2
    LEFT = 3
    RIGHT = 1
    TOP = 0

    def __init__(self, symbol: str):
        self.symbol = symbol

        self.exits = [False, False, False, False]
        self.start = False

        self._calculate()
    
    def _calculate(self):
        match self.symbol:
            case '|':
                self.exits = [True, False, True, False]
            case '-':
                self.exits = [False, True, False, True]
            case 'L':
                self.exits = [True, True, False, False]
            case 'J':
                self.exits = [True, False, False, True]
            case '7':
                self.exits = [False, False, True, True]
            case 'F':
                self.exits = [False, True, True, False]
            case 'S':
                self.start = True

    def dump(self) -> str:
        return f'Pipe: {self.symbol} ' \
                f'T:{self.exits[self.TOP]}, ' \
                f'R:{self.exits[self.RIGHT]}, ' \
                f'B:{self.exits[self.BOTTOM]}, ' \
                f'L:{self.exits[self.LEFT]}'

class Maze():

    def __init__(self):
        self._map = []
        self._start_x = 0
        self._start_y = 0
        self._current_x = 0
        self._current_y = 0
        self._last_entry = -1

    def add_row(self, row: str):
        self._map.append([])
        current_y = len(self._map) - 1
        
        for symbol in [*row]:
            pipe_segment = Pipe(symbol)
            self._map[current_y].append(pipe_segment)

            if pipe_segment.start:
                self._start_x = len(self._map[current_y]) - 1
                self._start_y = current_y

    def _calculate_starter(self):
        self._current_x = self._start_x
        self._current_y = self._start_y
        self._map[self._start_y][self._start_x].exits = [
            self._map[self._start_y - 1][self._start_x].exits[Pipe.BOTTOM],
            self._map[self._start_y][self._start_x + 1].exits[Pipe.LEFT],
            self._map[self._start_y + 1][self._start_x].exits[Pipe.TOP],
            self._map[self._start_y][self._start_x - 1].exits[Pipe.RIGHT]
        ]

    def dump(self) -> str:
        results = 'Full Map:\n'

        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                results += f'{self._map[y][x].symbol}'
            results += '\n'
        
        results += f'Starting Position: {self._start_x}:{self._start_y}'
        
        return results

    def _invert(direction_out: int):
        match direction_out:
            case Pipe.TOP:
                return Pipe.BOTTOM
            case Pipe.RIGHT:
                return Pipe.LEFT
            case Pipe.BOTTOM:
                return Pipe.TOP
            case Pipe.LEFT:
                return Pipe.RIGHT

    def _get_pipe(self, y: int, x: int) -> Pipe:
        try:
            return self._map[y][x]
        except:
            return None

    def get_steps(self) -> int:

        self._calculate_starter()

        total_steps = 0
        keep_going = True
        while keep_going:

            current_block = self._map[self._current_y][self._current_x]

            print(f'{current_block.dump()} = {self._current_y}:{self._current_x}')

            if current_block.exits[Pipe.TOP] and self._last_entry != Pipe.TOP:
                print(f'checking UP')
                next_block = self._get_pipe(self._current_y - 1, self._current_x)
                print(next_block.dump())
                if next_block and next_block.exits[Pipe.BOTTOM]:
                    print(f'moving UP')
                    self._current_y -= 1
                    self._last_entry = Pipe.BOTTOM
            
            elif current_block.exits[Pipe.RIGHT] and self._last_entry != Pipe.RIGHT:
                print(f'checking RIGHT')
                next_block = self._get_pipe(self._current_y, self._current_x + 1)
                print(next_block.dump())
                if next_block and next_block.exits[Pipe.LEFT]:
                    print(f'moving RIGHT')
                    self._current_x += 1
                    self._last_entry = Pipe.LEFT

            elif current_block.exits[Pipe.BOTTOM] and self._last_entry != Pipe.BOTTOM:
                print(f'checking DOWN')
                next_block = self._get_pipe(self._current_y + 1, self._current_x)
                print(next_block.dump())
                if next_block and next_block.exits[Pipe.TOP]:
                    print(f'moving DOWN')
                    self._current_y += 1
                    self._last_entry = Pipe.TOP

            elif current_block.exits[Pipe.LEFT] and self._last_entry != Pipe.LEFT:
                print(f'checking LEFT')
                next_block = self._get_pipe(self._current_y, self._current_x - 1)
                print(next_block.dump())
                if next_block and next_block.exits[Pipe.RIGHT]:
                    print(f'moving LEFT')
                    self._current_x -= 1
                    self._last_entry = Pipe.RIGHT

            total_steps += 1

            if self._current_x == self._start_x and self._current_y == self._start_y:
                keep_going = False

        return total_steps

#
# MAIN
#

maze = Maze()

with open('input.txt') as input_file:
    for input_row in input_file:
        maze.add_row(input_row.strip())

total_steps = maze.get_steps()

print(f'Total Steps: {total_steps}')
print(f'Furthest Point: {total_steps / 2}')

################################################################################
# END
################################################################################
