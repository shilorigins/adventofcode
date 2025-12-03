import re

filepath = "02.test"
#filepath = "02.input"


def part01(ranges):
    count = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            s = str(n)
            hasEvenLength = len(s) % 2 == 0
            halvesMatch = s[:len(s) // 2] == s[len(s) // 2:]
            if hasEvenLength and halvesMatch:
                count += n
    return count


def isInvalid(s):
    for i in range(1, len(s) // 2 + 1):
        multiple = len(s) // i
        if multiple == len(s) / i:
            if s[:i] * multiple == s:
                return True
    return False


def part02(ranges):
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            total += isInvalid(str(n)) * n
    return total


if __name__ == "__main__":
    with open(filepath) as f:
        ranges = []
        for line in f.read().split('\n')[:-1]:
            m = re.match(r"(\d*)-(\d*)", line)
            ranges.append((int((m.group(1))), int(m.group(2))))
    print("Part 01: ", part01(ranges))
    print("Part 02: ", part02(ranges))
