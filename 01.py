#filepath = "01.test"
filepath = "01.input"


def part01():
    left = []
    right = []
    with open(filepath) as f:
        for line in f.readlines():
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
    diff = 0
    for l, r in zip(sorted(left), sorted(right)):
        diff += abs(l - r)
    print(diff)


def part02():
    from collections import defaultdict
    left_counts = defaultdict(int)
    right_counts = defaultdict(int)
    with open(filepath) as f:
        for line in f.readlines():
            l, r = line.split()
            left_counts[l] += 1
            right_counts[r] += 1
    total = 0
    for num, count in left_counts.items():
        total += int(num) * count * right_counts[num]
    print(total)
    

if __name__ == "__main__":
    part01()
    part02()
