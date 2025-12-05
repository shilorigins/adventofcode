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
    contiguous = set()
    for lower, upper in ranges:
        overridden = []
        for c in contiguous:
            if lower <= c[0]:
                if upper <= c[0]:
                    pass
                elif upper <= c[1]:
                    upper = c[1]
                    overridden.append(c)
                elif upper >= c[1]:
                    overridden.append(c)
            elif lower <= c[1]:
                if upper <= c[1]:
                    lower = c[0]
                    upper = c[1]
                    overridden.append(c)
                else:
                    lower = c[0]
                    overridden.append(c)
        for elem in overridden:
            contiguous.remove(elem)
        contiguous.add((lower, upper))
    count = 0
    for lower, upper in contiguous:
        count += upper - lower + 1
    return count


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
