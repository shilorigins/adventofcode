import re
from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def part01(text):
    text = re.sub(r' +', ',', text)
    rows = [row.strip(',').split(',') for row in text.split('\n')[:-1]]
    total = 0
    for *numbers, op in zip(*rows):
        if op == '+':
            total += sum([int(n) for n in numbers])
        elif op == '*':
            subtotal = 1
            for n in numbers:
                subtotal *= int(n)
            total += subtotal
    return total


def part02(text):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        text = f.read()
    print("Part 01: ", part01(text))
    print("Part 02: ", part02(text))
