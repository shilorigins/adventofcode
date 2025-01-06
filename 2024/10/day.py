import sys
import os.path


def get_trailheads(topo):
    trailheads = set()
    for i, row in enumerate(topo):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.add((i, j))
    return trailheads


def get_adjacent(topo, point):
    i, j = point
    adjacent = [
        (i - 1, j),
        (i, j - 1),
        (i + 1, j),
        (i, j + 1)
    ]
    return ((x, y) for x, y in adjacent if (x >= 0
                                            and x < len(topo)
                                            and y >= 0
                                            and y < len(topo[0])))


def part01(topo):
    trailheads = get_trailheads(topo)
    trails = []
    q = [[trailhead] for trailhead in trailheads]
    while len(q) > 0:
        trail = q.pop()
        point = trail[-1]
        height = topo[point[0]][point[1]]
        if height == 9:
            trails.append(trail)
        else:
            adjacent = get_adjacent(topo, point)
            q.extend([trail + [point] for point in adjacent if topo[point[0]][point[1]] == height + 1])
    return trails


def part02(topo):
    pass


def print_trails(trails):
    from pprint import pprint
    for trail in trails:
        print("\n".join(["".join(['#' if (i, j) in trail else str(topo[i][j]) for j in range(len(topo[i]))]) for i in range(len(topo))]))
        print('\n')


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    match sys.argv[1]:
        case "toy":
            filepath = stem + '.toy'
        case "test":
            filepath = stem + '.test'
        case "input":
            filepath = stem + '.input'
    with open(filepath) as f:
        topo = [[int(c) for c in row] for row in f.read().split()]
    trails = part01(topo)
    start_end_pairs = set([(trail[0], trail[-1]) for trail in trails])
    print(len(start_end_pairs))
    print(len(trails))
