import heapq
import math
import sys

from copy import deepcopy
from enum import Enum, auto
from pprint import pprint


class Facing(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Path:
    def __init__(self, maze, path, facing):
        self.maze = maze
        self.path = path
        self.facing = facing

    @property
    def head(self):
        index = -1
        head = self.path[index]
        while isinstance(head, Facing):
            index -= 1
            head = self.path[index]
        return head

    @property
    def score(self):
        return sum([1000 if isinstance(step, Facing) else 1 for step in self.path]) - 1

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        else:
            return self.score < other.score

    def print(self):
        copy = deepcopy(self.maze)
        char = '>'
        for step in self.path:
            match step:
                case Facing.LEFT:
                    char = '<'
                case Facing.RIGHT:
                    char = '>'
                case Facing.UP:
                    char = '^'
                case Facing.DOWN:
                    char = 'v'
                case _:
                    copy[step[0]][step[1]] = char
        pprint(["".join(line) for line in copy])


def part01(maze):
    lowest = math.inf
    start = None
    end = None
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == 'S':
                start = (i, j)
            if char == 'E':
                end = (i, j)
    q = []
    path = Path(maze, [start], Facing.RIGHT)
    while path.head != end:
        match path.facing:
            case Facing.LEFT:
                new_path = Path(path.maze, path.path + [Facing.UP], Facing.UP)
                heapq.heappush(q, new_path)
                new_path = Path(path.maze, path.path + [Facing.DOWN], Facing.DOWN)
                heapq.heappush(q, new_path)
                new_head = (path.head[0], path.head[1] - 1)
                new_path = Path(path.maze, path.path + [new_head], Facing.LEFT)
                if maze[new_head[0]][new_head[1]] != '#':
                    heapq.heappush(q, new_path)
            case Facing.RIGHT:
                new_path = Path(path.maze, path.path + [Facing.UP], Facing.UP)
                heapq.heappush(q, new_path)
                new_path = Path(path.maze, path.path + [Facing.DOWN], Facing.DOWN)
                heapq.heappush(q, new_path)
                new_head = (path.head[0], path.head[1] + 1)
                new_path = Path(path.maze, path.path + [new_head], Facing.RIGHT)
                if maze[new_head[0]][new_head[1]] != '#':
                    heapq.heappush(q, new_path)
            case Facing.UP:
                new_path = Path(path.maze, path.path + [Facing.LEFT], Facing.LEFT)
                heapq.heappush(q, new_path)
                new_path = Path(path.maze, path.path + [Facing.RIGHT], Facing.RIGHT)
                heapq.heappush(q, new_path)
                new_head = (path.head[0] - 1, path.head[1])
                new_path = Path(path.maze, path.path + [new_head], Facing.UP)
                if maze[new_head[0]][new_head[1]] != '#':
                    heapq.heappush(q, new_path)
            case Facing.DOWN:
                new_path = Path(path.maze, path.path + [Facing.LEFT], Facing.LEFT)
                heapq.heappush(q, new_path)
                new_path = Path(path.maze, path.path + [Facing.RIGHT], Facing.RIGHT)
                heapq.heappush(q, new_path)
                new_head = (path.head[0] + 1, path.head[1])
                new_path = Path(path.maze, path.path + [new_head], Facing.DOWN)
                if maze[new_head[0]][new_head[1]] != '#':
                    heapq.heappush(q, new_path)
        path = heapq.heappop(q)
    return path.score


def part02():
    pass


def test_smaller():
    with open('test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01(maze) == 7036
    assert part02() is None


def test_bigger():
    with open('bigger_test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01(maze) == 11048
    assert part02() is None


def main():
    with open('input.txt') as f:
        _ = f.read().split()
    print(part01())
    print(part02())


if __name__ == "__main__":
    main()
