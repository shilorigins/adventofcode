from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def part01(ranges, ingredients):
    pass


def part02(ranges, ingredients):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        first, second = f.read().split('\n\n')
        ranges, ingredients = first.split('\n'), [int(s) for s in second.split('\n')[:-1]]
    print("Part 01: ", part01(ranges, ingredients))
    print("Part 02: ", part02(ranges, ingredients))
