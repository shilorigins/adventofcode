import sys
from enum import IntEnum, auto


class Letter(IntEnum):
    X = 0
    M = auto()
    A = auto()
    S = auto()


def collect_path_starts(grid, letter):
    locations = []
    for i, row in enumerate(grid):
        search_start = 0
        while (j := row.find(letter.name, search_start)) >= 0:
            for direction in range(1, 9):
                locations.append((direction, [(i, j)]))
            search_start = j + 1
    return locations


def near_points(i, j):
    points = [
        (i-1, j-1),
        (i-1, j),
        (i-1, j+1),
        (i, j-1),
        (i, j+1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1),
    ]
    for point in points:
        if point[0] < 0 or point[1] < 0:
            points.remove(point)
    return points


def get_point(point, direction):
    match direction:
        case 1:
            new_point = (point[0]-1, point[1]-1)
        case 2:
            new_point = (point[0]-1, point[1])
        case 3:
            new_point = (point[0]-1, point[1]+1)
        case 4:
            new_point = (point[0], point[1]-1)
        case 5:
            new_point = (point[0], point[1]+1)
        case 6:
            new_point = (point[0]+1, point[1]-1)
        case 7:
            new_point = (point[0]+1, point[1])
        case 8:
            new_point = (point[0]+1, point[1]+1)
    if new_point[0] < 0 or new_point[1] < 0:
        raise IndexError
    return new_point


def part01(grid):
    paths = collect_path_starts(grid, Letter.X)
    for letter in Letter:
        if letter.name == 'X':
            continue
        active_paths = []
        for direction, path in paths:
            try:
                x, y = get_point(path[letter-1], direction)
                if grid[x][y] == letter.name:
                    active_paths.append((direction, path + [(x, y)]))
            except IndexError:
                pass
        paths = active_paths
    return len(paths)
                


def part02(grid):
    paths = collect_path_starts(grid, Letter.M)
    paths = [path for path in paths if path[0] in [1, 3, 6, 8]]
    for letter in Letter:
        if letter <= Letter.M:
            continue
        active_paths = []
        for direction, path in paths:
            try:
                x, y = get_point(path[letter-2], direction)
                if grid[x][y] == letter.name:
                    active_paths.append((direction, path + [(x, y)]))
            except IndexError:
                pass
        paths = active_paths
    middles = [path[1] for _, path in paths]
    count = 0
    seen = set()
    for point in middles:
        if point in seen:
            count += 1
        else:
            seen.add(point)
    return count


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        grid = f.readlines()
    print(part02(grid))
