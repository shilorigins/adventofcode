import heapq
import math
import sys

from collections import deque
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
        if path.facing == Facing.LEFT:
            rotate_cw = Path(path.maze, path.path + [Facing.UP], Facing.UP)
            rotate_ccw = Path(path.maze, path.path + [Facing.DOWN], Facing.DOWN)
            new_head = (path.head[0], path.head[1] - 1)
        elif path.facing == Facing.RIGHT:
            rotate_ccw = Path(path.maze, path.path + [Facing.UP], Facing.UP)
            rotate_cw = Path(path.maze, path.path + [Facing.DOWN], Facing.DOWN)
            new_head = (path.head[0], path.head[1] + 1)
        elif path.facing == Facing.UP:
            rotate_ccw = Path(path.maze, path.path + [Facing.LEFT], Facing.LEFT)
            rotate_cw = Path(path.maze, path.path + [Facing.RIGHT], Facing.RIGHT)
            new_head = (path.head[0] - 1, path.head[1])
        elif path.facing == Facing.DOWN:
            rotate_ccw = Path(path.maze, path.path + [Facing.LEFT], Facing.LEFT)
            rotate_cw = Path(path.maze, path.path + [Facing.RIGHT], Facing.RIGHT)
            new_head = (path.head[0] + 1, path.head[1])
        if not isinstance(path.head, Facing):  # there's never a reason to turn twice
            heapq.heappush(q, rotate_cw)
            heapq.heappush(q, rotate_ccw)
        if maze[new_head[0]][new_head[1]] != '#':
            heapq.heappush(q, Path(path.maze, path.path + [new_head], path.facing))
        path = heapq.heappop(q)
    return path.score


def adjacent(point, maze):
    i, j = point
    height = len(maze)
    width = len(maze[0])
    points = (
        ((i - 1, j), Facing.UP),
        ((i, j - 1), Facing.LEFT),
        ((i + 1, j), Facing.DOWN),
        ((i, j + 1), Facing.RIGHT),
    )
    return (step for step in points if step[0][0] >= 0 and step[0][0] < height and step[0][1] >= 0 and step[0][1] < width and maze[step[0][0]][step[0][1]] != '#')


def print_scores(maze, dp):
    scores = deepcopy(maze)
    for i in range(len(scores)):
        for j in range(len(scores[0])):
            if dp[i][j][0] != math.inf:
                scores[i][j] = str(dp[i][j][0]).center(5)
            else:
                scores[i][j] = scores[i][j].center(5)
    pprint(["".join(line) for line in scores])


def print_path(maze, dp, point):
    copy = deepcopy(maze)
    char = '@'
    while maze[point[0]][point[1]] != 'E':
        _, step_direction = dp[point[0]][point[1]]
        match step_direction:
            case Facing.LEFT:
                char = '<'
                point = (point[0], point[1] - 1)
            case Facing.RIGHT:
                char = '>'
                point = (point[0], point[1] + 1)
            case Facing.UP:
                char = '^'
                point = (point[0] - 1, point[1])
            case Facing.DOWN:
                char = 'v'
                point = (point[0] + 1, point[1])
        copy[point[0]][point[1]] = char
    pprint(["".join(line) for line in copy])


def print_paths(maze, dp):
    copy = deepcopy(maze)
    char = '@'
    for i in range(len(copy)):
        for j in range(len(copy[0])):
            match dp[i][j][1]:
                case Facing.LEFT:
                    char = '<'
                case Facing.RIGHT:
                    char = '>'
                case Facing.UP:
                    char = '^'
                case Facing.DOWN:
                    char = 'v'
                case _:
                    char = copy[i][j]
            copy[i][j] = char
    pprint(["".join(line) for line in copy])


def part01_dynamic(maze) -> int:
    dp = [[(math.inf, None) for _ in range(len(maze[0]))] for _ in range(len(maze))]
    j = len(maze[0])
    for i, row in enumerate(maze):
        try:
            j = row.index('E')
            break
        except ValueError:
            pass
    end = (i, j)
    start = None
    dp[end[0]][end[1]] = (0, None)
    q = set([point for point, _ in adjacent(end, maze)])
    while len(q) > 0:
        point = q.pop()
        if maze[point[0]][point[1]] == 'S':
            start = point
        step_cost = {}
        for neighbor, step_direction in adjacent(point, maze):
            if dp[neighbor[0]][neighbor[1]][0] != math.inf:
                cost = dp[neighbor[0]][neighbor[1]][0] + 1
                if step_direction != dp[neighbor[0]][neighbor[1]][1] and dp[neighbor[0]][neighbor[1]][1] is not None:
                    cost += 1000
                step_cost[neighbor] = (cost, step_direction)
        lowest = math.inf
        facing = None
        for neighbor in step_cost:
            if step_cost[neighbor][0] < lowest:
                lowest = step_cost[neighbor][0]
                facing = step_cost[neighbor][1]
        dp[point[0]][point[1]] = (lowest, facing)
        for neighbor, _ in adjacent(point, maze):
            if dp[neighbor[0]][neighbor[1]][0] > lowest:
                q.add(neighbor)
    inital_turn_cost = 0
    match dp[start[0]][start[1]][1]:
        case Facing.UP:
            inital_turn_cost = 1000
        case Facing.DOWN:
            inital_turn_cost = 1000
        case Facing.LEFT:
            inital_turn_cost = 2000
    return dp[start[0]][start[1]][0] + inital_turn_cost


def part02():
    pass


def test_smaller():
    with open('test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01_dynamic(maze) == 7036
    assert part02() is None


def test_bigger():
    with open('bigger_test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01_dynamic(maze) == 11048
    assert part02() is None


def main():
    with open('input.txt') as f:
        maze = [list(line) for line in f.read().split()]
    print(part01(maze))
    print(part02())


if __name__ == "__main__":
    main()
