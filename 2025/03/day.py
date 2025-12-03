filepath = "03.test"
#filepath = "03.input"


def part01(banks):
    joltage = 0
    for bank in banks:
        first_digit = max(bank)
        i = bank.index(first_digit)
        if i == len(bank) - 1:
            second_digit = first_digit
            first_digit = max(bank[:-1])
        else:
            second_digit = max(bank[i+1:])
        joltage += first_digit * 10 + second_digit
    return joltage


def part02(banks):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        banks = [[int(c) for c in bank] for bank in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(banks))
    print("Part 02: ", part02(banks))
