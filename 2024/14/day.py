import sys
import os.path
import re
from copy import deepcopy
from pprint import pprint


def part01(robots):
    height = 103
    width = 101
    iterations = 100
    quadrants = [0 for _ in range(4)]
    for robot in robots:
        pos = robot[0]
        vel = robot[1]
        pos[0] = (pos[0] + vel[0]*iterations) % width
        pos[1] = (pos[1] + vel[1]*iterations) % height
        #pos[0] %= height
        #pos[1] %= width
        if pos[0] < width // 2:
            if pos[1] < height // 2:
                quadrants[0] += 1
            elif pos[1] > height // 2:
                quadrants[2] += 1
        elif pos[0] > width // 2:
            if pos[1] < height // 2:
                quadrants[1] += 1
            elif pos[1] > height // 2:
                quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part02(robots):
    height = 103
    width = 101
    iterations = 100
    grid = [['.' for j in range(width)] for i in range(height)]

    with open("14.graphs", 'w') as f:
        pass
    for count in range(iterations):
        for robot in robots:
            pos = robot[0]
            vel = robot[1]
            pos[0] = (pos[0] + vel[0]) % width
            pos[1] = (pos[1] + vel[1]) % height
        image = deepcopy(grid)
        for robot in robots:
            image[robot[0][1]][robot[0][0]] = '#'
        for i in range(len(image)):
            image[i] = "".join(image[i])
        with open("14.graphs", 'a') as f:
            print(f"Iteration: {count}", file=f)
            pprint(image, stream=f)


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    machines = []
    robots = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            m = re.match(r"p=([0-9,-]+) v=([0-9,-]+)", line)
            pos = [int(i) for i in m.group(1).split(',')]
            vel = [int(i) for i in m.group(2).split(',')]
            robots.append([pos, vel])
    score = part01(robots)
    print(score)
    part02(robots)
    print('Inspect 14.graphs for the answer')
