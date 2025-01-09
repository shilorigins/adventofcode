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
    def __init__(self, maze, path, head, facing):
        self.maze = maze
        self.tail = path
        self.head = head
        self.facing = facing

    @property
    def score(self):
        if self.tail == []:
            return 1
        else:
            return self.tail.score + 1 + 1000*(self.tail.facing != None and self.facing == self.tail.facing)

    @property
    def points(self):
        if self.tail == []:
            return set()
        else:
            return self.tail.points | {self.head}

    def print(self):
        copy = deepcopy(self.maze)
        char = '@'
        for i, j in self.points:
            copy[i][j] = char
        pprint(["".join(line) for line in copy])

    def __contains__(self, point):
        return self.head == point or point in self.tail


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
    return tuple(step for step in points if step[0][0] >= 0 and step[0][0] < height and step[0][1] >= 0 and step[0][1] < width and maze[step[0][0]][step[0][1]] != '#')


def print_scores(maze, dp):
    scores = deepcopy(maze)
    for i in range(len(scores)):
        for j in range(len(scores[0])):
            if dp[i][j][0] != math.inf:
                scores[i][j] = str(dp[i][j][0]).center(5)
            else:
                scores[i][j] = scores[i][j].center(5)
    pprint(["".join(line) for line in scores])


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


def find_char(maze, char):
    j = len(maze[0])
    for i, row in enumerate(maze):
        try:
            j = row.index(char)
            break
        except ValueError:
            pass
    return i, j


def compute_cost_grid(maze):
    dp = [[(math.inf, None) for _ in range(len(maze[0]))] for _ in range(len(maze))]
    end = find_char(maze, 'E')
    dp[end[0]][end[1]] = (0, None)
    q = set([point for point, _ in adjacent(end, maze)])
    while len(q) > 0:
        point = q.pop()
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
    start = find_char(maze, 'S')
    inital_turn_cost = 0
    match dp[start[0]][start[1]][1]:
        case Facing.UP:
            inital_turn_cost = 1000
        case Facing.DOWN:
            inital_turn_cost = 1000
        case Facing.LEFT:
            inital_turn_cost = 2000
    dp[start[0]][start[1]] = (dp[start[0]][start[1]][0] + inital_turn_cost, dp[start[0]][start[1]][1])
    return dp


def part01_dynamic(maze):
    dp = compute_cost_grid(maze)
    i, j = find_char(maze, 'S')
    return dp[i][j][0]


def print_good_seats(maze, good_seats):
    copy = deepcopy(maze)
    for i, j in good_seats:
        copy[i][j] = 'O'
    pprint(["".join(line) for line in copy])


def part02(maze):
    dp = compute_cost_grid(maze)
    q = [find_char(maze, 'S')]
    good_seats = set(q)
    while len(q) > 0:
        point = q.pop()
        if maze[point[0]][point[1]] == 'E':
            continue
        #steps = [step for step in adjacent(point, maze) if step[0] not in good_seats]
        steps = adjacent(point, maze)
        optimal_cost = min([dp[neighbor[0]][neighbor[1]][0] for neighbor, _ in steps])
        for neighbor, _ in steps:
            if dp[neighbor[0]][neighbor[1]][0] == optimal_cost or dp[neighbor[0]][neighbor[1]][0] - 1000 == optimal_cost:
                good_seats.add(neighbor)
                q.append(neighbor)
    print_good_seats(maze, good_seats)
    return len(good_seats)


def part02_path_finding(maze):
    lowest = math.inf
    start = find_char(maze, 'S')
    end = find_char(maze, 'E')

    paths = []
    q = [Path(maze, [], end, None)]
    while len(q) > 0:
        path = q.pop()
        if path.head == start:
            paths.append(path)
        else:
            for point, step_direction in adjacent(path.head, maze):
                if point not in path:
                    new_path = Path(maze, path, point, step_direction)
                    q.append(new_path)
    optimal_cost = min([path.score for path in paths])
    good_seats = set()
    for path in paths:
        if path.score == optimal_cost:
            good_seats |= path.points
    return len(good_seats)


def test_smaller():
    with open('test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01_dynamic(maze) == 7036
    assert part02_path_finding(maze) == 45


def test_bigger():
    with open('bigger_test.txt') as f:
        maze = [list(line) for line in f.read().split()]
    assert part01_dynamic(maze) == 11048
    assert part02_path_finding(maze) == 64


def main():
    with open('input.txt') as f:
        maze = [list(line) for line in f.read().split()]
    #print(part01_dynamic(maze))
    print(part02_path_finding(maze))


if __name__ == "__main__":
    main()
