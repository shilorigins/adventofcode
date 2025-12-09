from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def area(p1, p2):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)


def part01(tiles):
    largest = 0
    for tile in tiles:
        for other in tiles - {tile}:
            largest = max(largest, area(tile, other))
    return largest


def part02(tiles):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        tiles = set((int(x), int(y)) for x, y in (row.split(',') for row in f.read().split('\n')[:-1]))
    print("Part 01: ", part01(tiles))
    print("Part 02: ", part02(tiles))
