import sys
import os.path
from collections import defaultdict


def get_type_map(grid):
    types = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                types[grid[i][j]].add((i, j))
    return types


def part01(grid):
    types = get_type_map(grid)
    antinodes = set()
    for typ, points in types.items():
        points = list(points)
        for i, p1 in list(enumerate(points))[:-1]:
            for p2 in points[i+1:]:
                rise = p1[1] - p2[1]
                run = p1[0] - p2[0]
                antinode = (p1[0] + run, p1[1] + rise)
                if (antinode[0] >= 0
                    and antinode[0] < len(grid)
                    and antinode[1] >= 0
                    and antinode[1] < len(grid[0])
                ):
                    antinodes.add(antinode)
                antinode = (p2[0] - run, p2[1] - rise)
                if (antinode[0] >= 0
                    and antinode[0] < len(grid)
                    and antinode[1] >= 0
                    and antinode[1] < len(grid[0])
                ):
                    antinodes.add(antinode)
    return antinodes


def part02(grid):
    types = get_type_map(grid)
    antinodes = set()
    for typ, points in types.items():
        points = list(points)
        for i, p1 in list(enumerate(points))[:-1]:
            for p2 in points[i+1:]:
                antinodes.add(p1)
                antinodes.add(p2)
                rise = p1[1] - p2[1]
                run = p1[0] - p2[0]
                antinode = (p1[0] + run, p1[1] + rise)
                while (antinode[0] >= 0
                    and antinode[0] < len(grid)
                    and antinode[1] >= 0
                    and antinode[1] < len(grid[0])
                ):
                    antinodes.add(antinode)
                    antinode = (antinode[0] + run, antinode[1] + rise)
                antinode = (p2[0] - run, p2[1] - rise)
                while (antinode[0] >= 0
                    and antinode[0] < len(grid)
                    and antinode[1] >= 0
                    and antinode[1] < len(grid[0])
                ):
                    antinodes.add(antinode)
                    antinode = (antinode[0] - run, antinode[1] - rise)
    return antinodes


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    match sys.argv[1]:
        case "test":
            filepath = stem + '.test'
        case "input":
            filepath = stem + '.input'
    with open(filepath) as f:
        grid = [list(row) for row in f.read().strip().split()]
    antinodes = part01(grid)
    print(len(antinodes))
    antinodes = part02(grid)
    print(len(antinodes))
