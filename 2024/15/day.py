import sys
import os.path

from pprint import pprint


class Warehouse:
    def __init__(self, string):
        self.grid = [list(line) for line in string.split()]
        for i, line in enumerate(self.grid):
            try:
                self.robot = (i, line.index('@'))
                #line[self.robot[1]] = '.'
            except ValueError:
                pass

    def move(self, direction):
        start = None
        end = None
        match direction:
            case '<':
                start = (self.robot[0], self.robot[1] - 1)
                end = start
                while self.grid[end[0]][end[1]] == 'O':
                    end = (end[0], end[1] - 1)
            case '^':
                start = (self.robot[0] - 1, self.robot[1])
                end = start
                while self.grid[end[0]][end[1]] == 'O':
                    end = (end[0] - 1, end[1])
            case '>':
                start = (self.robot[0], self.robot[1] + 1)
                end = start
                while self.grid[end[0]][end[1]] == 'O':
                    end = (end[0], end[1] + 1)
            case 'v':
                start = (self.robot[0] + 1, self.robot[1])
                end = start
                while self.grid[end[0]][end[1]] == 'O':
                    end = (end[0] + 1, end[1])
        if self.grid[end[0]][end[1]] == '.':
            self.grid[end[0]][end[1]] = 'O'
            self.grid[start[0]][start[1]] = '@'
            self.grid[self.robot[0]][self.robot[1]] = '.'
            self.robot = start

    def gps(self) -> int:
        total = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'O':
                    total += i * 100 + j
        return total

    def __repr__(self):
        return "\n".join("".join(line) for line in self.grid)


class WideWarehouse(Warehouse):
    def __init__(self, string):
        pass

    def move(self, direction):
        pass


def part01(warehouse, moves) -> int:
    for direction in moves:
        warehouse.move(direction)
    return warehouse.gps()


def part02(warehouse, moves):
    pass


def test():
    with open('toy.txt') as f:
        warehouse_str, move_str = f.read().split('\n\n')
    warehouse = Warehouse(warehouse_str)
    moves = "".join(move_str.split())
    assert part01(warehouse, moves) == 2028
    wide_warehouse = WideWarehouse(warehouse_str)
    assert part02(wide_warehouse, moves)

    with open('test.txt') as f:
        warehouse_str, move_str = f.read().split('\n\n')
    warehouse = Warehouse(warehouse_str)
    moves = "".join(move_str.split())
    assert part01(warehouse, moves) == 10092
    wide_warehouse = WideWarehouse(warehouse_str)
    assert part02(wide_warehouse, moves)


def main():
    with open('input.txt') as f:
        warehouse_str, move_str = f.read().split('\n\n')
    warehouse = Warehouse(warehouse_str)
    moves = "".join(move_str.split())
    print(part01(warehouse, moves))


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test()
    else:
        main()
