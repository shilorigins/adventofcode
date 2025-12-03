filepath = "03.test"
#filepath = "03.input"


def part01(banks):
    pass


def part02(banks):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        banks = [[int(c) for c in bank] for bank in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(banks))
    print("Part 02: ", part02(banks))
