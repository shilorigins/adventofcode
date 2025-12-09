from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def part01(tiles):
    pass


def part02(tiles):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        tiles = set((int(x), int(y)) for x, y in (row.split(',') for row in f.read().split('\n')[:-1]))
    print("Part 01: ", part01(tiles))
    print("Part 02: ", part02(tiles))
