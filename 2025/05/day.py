import re
from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def part01(ranges, ingredients):
    count = 0
    for lower, upper in ranges:
        for ingredient in ingredients.copy():
            if ingredient >= lower and ingredient <= upper:
                count += 1
                ingredients.remove(ingredient)
    return count


def part02(ranges):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        first, second = f.read().split('\n\n')
        ranges, ingredients = first.split('\n'), set(int(s) for s in second.split('\n')[:-1])
        parsed_ranges = []
        for line in ranges:
            m = re.match(r"(\d*)-(\d*)", line)
            parsed_ranges.append((int(m.group(1)), int(m.group(2))))
    print("Part 01: ", part01(parsed_ranges, ingredients))
    print("Part 02: ", part02(parsed_ranges))
