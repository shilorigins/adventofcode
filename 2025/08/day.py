import heapq
import numpy
from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


class JunctionBox:
    def __init__(self, coordinates):
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])
        self.z = int(coordinates[2])

    def __str__(self):
        return f"JunctionBox(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"JunctionBox(x={self.x}, y={self.y}, z={self.z})"

    @staticmethod
    def distance(first, second):
        return numpy.sqrt((first.x - second.x)**2 + (first.y - second.y)**2 + (first.z - second.z)**2)

    def __hash__(self):
        return (self.x, self.y, self.z).__hash__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


def part01(boxes):
    sets = {}
    q = []
    for i, first in enumerate(boxes):
        sets[first] = i
        for second in boxes[i+1:]:
            heapq.heappush(q, (JunctionBox.distance(first, second), first, second))
    for _ in range(1000 if filepath == 'input.txt' else 10):
        _, first, second = heapq.heappop(q)
        old = min(sets[first], sets[second])
        new = max(sets[first], sets[second])
        sets[first] = new
        sets[second] = new
        for box, s in sets.items():
            if s == old:
                sets[box] = new
    counts = {}
    for s in sets.values():
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    largest = sorted(counts.values(), reverse=True)
    return largest[0] * largest[1] * largest[2]


def part02(boxes):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        boxes = [JunctionBox(row.split(',')) for row in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(boxes))
    print("Part 02: ", part02(boxes))
