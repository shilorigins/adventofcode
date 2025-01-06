import re
import sys


def part01(strings):
    pattern = r"mul\((\d+?),(\d+?)\)"
    total = 0
    for string in strings:
        matches = re.findall(pattern, string)
        for match_pair in matches:
            total += int(match_pair[0]) * int(match_pair[1])
    return total


def part02(strings):
    pattern = r"(do\(\))|(don't\(\))|mul\((\d+?),(\d+?)\)"
    enabled = True
    total = 0
    for string in strings:
        matches = re.findall(pattern, string)
        for match in matches:
            if match[0]:
                enabled = True
            elif match[1]:
                enabled = False
            elif enabled:
                total += int(match[2]) * int(match[3])
    return total


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        strings = f.readlines()
    print(part02(strings))
