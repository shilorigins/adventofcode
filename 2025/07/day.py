from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def part01(grid):
    beams = set()
    beams.add(grid[0].index('S'))
    count = 0
    for row in grid[1:]:
        split = set()
        splitters = {i for i, elem in enumerate(row) if elem == '^'}
        for splitter in splitters:
            try:
                beams.remove(splitter)
                split.add(splitter - 1)
                split.add(splitter + 1)
                count += 1
            except KeyError:
                pass
        beams |= split
    return count


def part02(grid):
    beams = {}
    beams[grid[0].index('S')] = 1
    for row in grid[2::2]:
        split = {}
        splitters = {i for i, elem in enumerate(row) if elem == '^'}
        for splitter in splitters:
            if splitter in beams:
                split[splitter - 1] = split.get(splitter - 1, 0) + beams[splitter]
                split[splitter + 1] = split.get(splitter + 1, 0) + beams[splitter]
                del beams[splitter]
        for beam in beams:
            if beam in split:
                split[beam] += beams[beam]
        beams.update(split)
    return sum(beams.values())


if __name__ == "__main__":
    with open(filepath) as f:
        grid = [list(row) for row in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(grid))
    print("Part 02: ", part02(grid))
