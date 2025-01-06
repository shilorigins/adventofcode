import sys
import os.path
from functools import cache


@cache
def num_solutions(design, patterns):
    if len(design) == 0:
        return 1
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += num_solutions(design.removeprefix(pattern), patterns)
    return count


def iter_num_solutions(design, patterns):
    count = 0
    q = [design]
    while len(q) > 0:
        design = q.pop()
        if len(design) == 0:
            count += 1
        else:
            for pattern in patterns:
                if design.startswith(pattern):
                    q.append(design.removeprefix(pattern))
    return count


def part01(designs, patterns):
    return sum(bool(num_solutions(design, patterns)) for design in designs)


def part02(designs, patterns):
    return sum(num_solutions(design, patterns) for design in designs)


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    with open(filepath) as f:
        patterns = frozenset(f.readline().split(', ')[:-1])
        f.readline()
        designs = f.read().split()
    possible_patterns = part01(designs, patterns)
    print(possible_patterns)
    possible_patterns = part02(designs, patterns)
    print(possible_patterns)
