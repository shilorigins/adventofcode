import sys
import os.path


class Path:
    def __init__(self, start, points=None):
        self.points = points.copy() if points else set()
        self.points.add(start)
        self.head = start

    def length(self):
        return len(self.points)


def find_start(grid):
    for i, row in enumerate(grid):
        try:
            return (i, row.index('S'))
        except ValueError:
            pass


def adjacent(point, grid):
    height = len(grid)
    width = len(grid[0])
    i, j = point
    points = [
        (i, j-1),
        (i-1, j),
        (i, j+1),
        (i+1, j),
    ]
    return (point for point in points if point[0] >= 0 and point[0] < height and point[1] >= 0 and point[1] < width)


def part01(grid):
    start = find_start(grid)
    paths = []
    q = [Path(start)]
    while len(q) > 0:
        active_path = q.pop()
        value = grid[active_path.head[0]][active_path.head[1]]
        if value == 'E':
            paths.append(active_path)
        elif value == '#':
            for point in teleport_points:
                if point not in active_path.points and grid[point[0]][point[1]] != '#':
                    new_path = Path(point, active_path.points)
                    q.append(new_path)
        else:
            adjacent_points = adjacent(active_path.head, grid)
            teleport_points = {point for point in adjacent(first, grid)}
            for point in adjacent_points:
                if point not in active_path.points and grid[point[0]][point[1]] != '#':
                    new_path = Path(point, active_path.points)
                    q.append(new_path)
    return paths


def part02(machines):
    pass


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    machines = []
    with open(filepath) as f:
        grid = f.read().splitlines()
    paths = part01(grid)
    honest = max(paths, key=lambda p: p.length())
    #cheats = set()
    #paths = []
    #for path in paths:
    #    if path.points not in cheats:
    #        cheats.add(frozenset(path.points))
    #        paths.append(path)
    #decent_cheats = [path for path in paths if len(path.points) < honest.length() - 100]
    decent_cheats = [path for path in paths if path.length() < honest.length()]
    deficits = [honest.length() - path.length() for path in decent_cheats]
    with open("20.graphs", 'w') as f:
        from pprint import pprint
        for path in decent_cheats:
            image = [list(row) for row in grid]
            for i, j in path.points:
                image[i][j] = ' '
            for i, j in path.cheats:
                image[i][j] = '@'
            image = ["".join(row) for row in image]
            print(f"Path: {honest.length() - path.length()} picoseconds saved", file=f)
            pprint(image, stream=f)
        pprint({length: deficits.count(length) for length in deficits})
