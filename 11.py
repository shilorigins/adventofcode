import sys
import os.path
from functools import cache


def naive(stones, iterations):
    while iterations > 0:
        for i, stone in enumerate(stones):
            if stone == 0:
                stones[i] == 1
            elif (length := len(str(stone))) % 2 == 0:
                stones[i:i+1] == int(str(stone)[:length//2]), int(str(stone)[length//2:])
            else:
                stones[i] *= 2024
    return stones


@cache
def count_expansions(stone, iterations):
    if iterations == 0:
        return 1
    if stone == 0:
        return count_expansions(1, iterations - 1)
    elif (length := len(str(stone))) % 2 == 0:
        return count_expansions(int(str(stone)[:length//2]), iterations - 1) + count_expansions(int(str(stone)[length//2:]), iterations - 1)
    else:
        return count_expansions(stone * 2024, iterations - 1)


def part01(stones, iterations):
    return sum([count_expansions(stone, iterations) for stone in stones])


def part02(stones):
    pass


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    match sys.argv[1]:
        case "test":
            filepath = stem + '.test'
        case "input":
            filepath = stem + '.input'
    with open(filepath) as f:
        stones = [int(c) for c in f.read().split()]
    num_stones = part01(stones, 25)
    print(num_stones)
    num_stones = part01(stones, 75)
    print(num_stones)
