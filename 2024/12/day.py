import sys
import os.path


class Side:
    def __init__(self, plots, crossing):
        target = plots[crossing[0][0]][crossing[0][1]]
        self.boundaries = set()
        self.boundaries.add(crossing)
        q = [crossing]
        while len(q) > 0:
            inner, outer = q.pop()
            if inner[0] == outer[0]:
                neighbors = (
                    ((inner[0] - 1, inner[1]), (outer[0] - 1, outer[1])),
                    ((inner[0] + 1, inner[1]), (outer[0] + 1, outer[1])),
                )
            else:
                neighbors = (
                    ((inner[0], inner[1] - 1), (outer[0], outer[1] - 1)),
                    ((inner[0], inner[1] + 1), (outer[0], outer[1] + 1)),
                )
            target = plots[inner[0]][inner[1]]
            for neighbor in neighbors:
                if neighbor in self.boundaries:
                    continue
                elif (neighbor[0][0] >= 0
                    and neighbor[0][0] < len(plots)
                    and neighbor[0][1] >= 0
                    and neighbor[0][1] < len(plots[0])
                    and plots[neighbor[0][0]][neighbor[0][1]] == target
                    and (neighbor[1][0] < 0
                    or neighbor[1][0] >= len(plots)
                    or neighbor[1][1] < 0
                    or neighbor[1][1] >= len(plots[0])
                    or plots[neighbor[1][0]][neighbor[1][1]] != target)
                ):
                    self.boundaries.add(neighbor)
                    q.append(neighbor)


class Region:
    def __init__(self, plots, point):
        target = plots[point[0]][point[1]]
        self.points = set()
        self.points.add(point)
        self.boundaries = set()
        q = [point]
        while len(q) > 0:
            point = q.pop()
            for neighbor in get_neighbors(point):
                if neighbor in self.points:
                    continue
                elif (neighbor[0] >= 0
                    and neighbor[0] < len(plots)
                    and neighbor[1] >= 0
                    and neighbor[1] < len(plots[0])
                    and plots[neighbor[0]][neighbor[1]] == target
                ):
                    self.points.add(neighbor)
                    q.append(neighbor)
                else:
                    self.boundaries.add((point, neighbor))

    def area(self):
        return len(self.points)

    def perimeter(self):
        return len(self.boundaries)

    def price(self):
        return self.area() * self.perimeter()

    def discount(self):
        sides = []
        for inner, outer in self.boundaries:
            inner_seen_before = False
            for side in sides:
                if (inner, outer) in side.boundaries:
                    inner_seen_before = True
            if not inner_seen_before:
                sides.append(Side(plots, (inner, outer)))
        return self.area() * len(sides)


def get_neighbors(point):
    i, j = point
    return (
        (i-1, j),
        (i, j-1),
        (i+1, j),
        (i, j+1),
    )


def part01(plots):
    regions = []
    for i in range(len(plots)):
        for j in range(len(plots[0])):
            point = (i, j)
            if not any([point in region.points for region in regions]):
                regions.append(Region(plots, point))
    return sum([region.price() for region in regions])


def part02(plots):
    regions = []
    for i in range(len(plots)):
        for j in range(len(plots[0])):
            point = (i, j)
            if not any([point in region.points for region in regions]):
                regions.append(Region(plots, point))
    return sum([region.discount() for region in regions])


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    with open(filepath) as f:
        plots = [list(row) for row in f.read().split()]
    price = part01(plots)
    print(price)
    price = part02(plots)
    print(price)
