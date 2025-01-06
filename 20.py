import sys
import os.path


class Path:
    def __init__(self, start, cheats=None, points=None):
        self.cheats = cheats.copy() if cheats else []
        self.points = points.copy() if points else set()
        self.head = start

    def length(self):
        return len(self.points) - 2 + len(self.cheats)


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
        for i, j in adjacent(active_path.head, grid):
            if (i, j) not in active_path.points and (i, j) not in active_path.cheats:
                value = grid[i][j]
                new_path = Path((i, j), active_path.cheats, active_path.points)
                if value == '.':
                    new_path.points.add((i, j))
                    q.append(new_path)
                elif value == '#' and len(active_path.cheats) < 2:
                    if len(active_path.cheats) == 0 or active_path.cheats[0] in adjacent(new_path.head, grid):
                        new_path.cheats.append((i, j))
                        q.append(new_path)
                elif value == 'E':
                    new_path.points.add((i, j))
                    paths.append(new_path)
    return paths


def part02(machines):
    pass


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    machines = []
    with open(filepath) as f:
        grid = f.read().splitlines()
    unique_paths = part01(grid)
    fastest_honest = min([path for path in unique_paths if len(path.cheats) == 0], key=lambda p: p.length())
    honest_record = len(fastest_honest.points)
    cheats = set()
    paths = []
    for path in unique_paths:
        if path.points not in cheats:
            cheats.add(frozenset(path.points))
            paths.append(path)
    #decent_cheats = [path for path in paths if len(path.points) < honest_record - 100]
    decent_cheats = [path for path in paths if path.length() < honest_record]
    deficits = [fastest_honest.length() - path.length() for path in decent_cheats]
    with open("20.graphs", 'w') as f:
        from pprint import pprint
        for path in decent_cheats:
            image = [list(row) for row in grid]
            for i, j in path.points:
                image[i][j] = ' '
            for i, j in path.cheats:
                image[i][j] = '@'
            image = ["".join(row) for row in image]
            print(f"Path: {fastest_honest.length() - path.length()} picoseconds saved", file=f)
            pprint(image, stream=f)
        pprint({length: deficits.count(length) for length in deficits})
