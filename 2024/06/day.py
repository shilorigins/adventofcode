import sys
from enum import Enum


class Facing(Enum):
    RIGHT = '>'
    LEFT = '<'
    UP = '^'
    DOWN = 'v'


class Guard:
    def __init__(self, grid):
        for facing in Facing:
            for i, row in enumerate(grid):
                try:
                    j = row.index(facing.value)
                except ValueError:
                    pass
                else:
                    if j >= 0:
                        self.row = i
                        self.column = j
                        self.facing = facing 
        self.grid = grid
        self.traversed = set()

    def is_obstructed(self):
        try:
            match self.facing:
                case Facing.RIGHT:
                    char = self.grid[self.row][self.column+1]
                case Facing.LEFT:
                    char = self.grid[self.row][self.column-1]
                case Facing.UP:
                    char = self.grid[self.row-1][self.column]
                case Facing.DOWN:
                    char = self.grid[self.row+1][self.column]
        except IndexError:
            char = ''
        return char == '#'

    def turn(self):
        match self.facing:
            case Facing.RIGHT:
                self.facing = Facing.DOWN
            case Facing.LEFT:
                self.facing = Facing.UP
            case Facing.UP:
                self.facing = Facing.RIGHT
            case Facing.DOWN:
                self.facing = Facing.LEFT
        self.grid[self.row][self.column] = self.facing.value

    def advance(self):
        self.grid[self.row][self.column] = '.'
        match self.facing:
            case Facing.RIGHT:
                self.column += 1
            case Facing.LEFT:
                self.column -= 1
            case Facing.UP:
                self.row -= 1
            case Facing.DOWN:
                self.row += 1
        if (self.row < 0
            or self.row >= len(grid)
            or self.column < 0
            or self.column >= len(grid[0])
        ):
            raise IndexError
        else:
            self.traversed.add((self.row, self.column))
            self.grid[self.row][self.column] = self.facing.value


def part01(grid):
    guard = Guard(grid)
    try:
        while True:
            while not guard.is_obstructed():
                guard.advance()
            guard.turn()
    except IndexError:
        return guard.traversed


def part02():
    pass


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        grid = [list(string) for string in f.read().split()]
    traversed = part01(grid)
    print(len(traversed))
