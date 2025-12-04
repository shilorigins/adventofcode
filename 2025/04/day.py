filepath = "test.txt"
#filepath = "input.txt"


def part01(grid):
    pass


def part02(grid):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        grid = [list(row) for row in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(grid))
    print("Part 02: ", part02(grid))
