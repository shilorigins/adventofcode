from pprint import pprint

filepath = "test.txt"
#filepath = "input.txt"


def area(p1, p2):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)


def part01(tiles):
    largest = 0
    for tile in tiles:
        for other in tiles - {tile}:
            largest = max(largest, area(tile, other))
    return largest


def interpolateGreen(redTiles):
    redAndGreenTiles = set()
    cursor = redTiles.pop(0)
    redTiles.append(cursor)
    redAndGreenTiles.add(cursor)
    for tile in redTiles[1:]:
        while cursor[0] - tile[0] > 0:
            cursor = (cursor[0] - 1, cursor[1])
            redAndGreenTiles.add(cursor)
        while tile[0] - cursor[0] > 0:
            cursor = (cursor[0] + 1, cursor[1])
            redAndGreenTiles.add(cursor)
        while cursor[1] - tile[1] > 0:
            cursor = (cursor[0], cursor[1] - 1)
            redAndGreenTiles.add(cursor)
        while tile[1] - cursor[1] > 0:
            cursor = (cursor[0], cursor[1] + 1)
            redAndGreenTiles.add(cursor)
    return redAndGreenTiles


def pour(p1, p2, perimeter):
    width = max((tile[0] for tile in perimeter)) + 1
    height = max((tile[1] for tile in perimeter)) + 1
    midpoint = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    if midpoint in perimeter:
        return False
    seen = perimeter.copy()
    q = [midpoint]
    while len(q) > 0:
        point = q.pop()
        if point[0] < 0 or point[0] > width or point[1] < 0 or point[1] > height:
            #printGrid(seen, p1, p2)
            return False
        seen.add(point)
        for point in (
            (point[0] - 1, point[1]),
            (point[0] + 1, point[1]),
            (point[0], point[1] - 1),
            (point[0], point[1] + 1)
        ):
            if point not in seen:
                q.append(point)
    #print(area(p1, p2))
    #printGrid(seen, p1, p2)
    return True


def printGrid(tiles, start=None, end=None):
    grid = [['.' for _ in range(max((tile[0] for tile in tiles)) + 1)] for _ in range(max((tile[1] for tile in tiles)) + 1)]
    for tile in tiles:
        grid[tile[1]][tile[0]] = 'X'
    if start:
        grid[start[1]][start[0]] = '#'
    if end:
        grid[end[1]][end[0]] = '#'
    pprint(["".join(row) for row in grid])
    print('\n')


def part02(redTiles):
    perimeter = interpolateGreen(tiles)
    largest = 0
    for redTile in redTiles:
        for other in redTiles:
            if pour(redTile, other, perimeter):
                largest = max(largest, area(redTile, other))
    return largest


if __name__ == "__main__":
    with open(filepath) as f:
        tiles = list((int(x), int(y)) for x, y in (row.split(',') for row in f.read().split('\n')[:-1]))
    print("Part 01: ", part01(set(tiles)))
    print("Part 02: ", part02(tiles))
