from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def propogate(char, counts, row, column, increment=True):
    height = len(counts)
    width = len(counts[0])
    for i, j in [
        (row-1, column-1),
        (row, column-1),
        (row+1, column-1),
        (row-1, column),
        (row+1, column),
        (row-1, column+1),
        (row, column+1),
        (row+1, column+1),
    ]:
        if i >= 0 and i < width and j >= 0 and j < width:
            if char == "@":
                if increment:
                    counts[j][i] += 1
                else:
                    counts[j][i] -= 1


def part01(grid, counts):
    return len([1 for j in range(len(counts)) for i in range(len(counts[0])) if counts[j][i] < 4 and grid[j][i] == "@"])


def part02(grid, counts):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        grid = [list(row) for row in f.read().split('\n')[:-1]]
    counts = [[0 for _ in row] for row in grid]
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == '@':
                propogate(grid[j][i], counts, i, j)
    print("Part 01: ", part01(grid, counts))
    print("Part 02: ", part02(grid, counts))
