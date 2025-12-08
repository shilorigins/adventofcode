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


def part01(boxes):
    pass


def part02(boxes):
    pass


if __name__ == "__main__":
    with open(filepath) as f:
        boxes = [JunctionBox(row.split(',')) for row in f.read().split('\n')[:-1]]
    print("Part 01: ", part01(boxes))
    print("Part 02: ", part02(boxes))
