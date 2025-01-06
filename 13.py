import sys
import os.path
import re


class Machine:
    pattern = r".* X[+=](\d+), Y[+=](\d+)"

    def __init__(self, a_line, b_line, prize_line):
        match = re.match(self.pattern, a_line)
        self.a = (int(match.group(1)), int(match.group(2)))
        match = re.match(self.pattern, b_line)
        self.b = (int(match.group(1)), int(match.group(2)))
        match = re.match(self.pattern, prize_line)
        self.prize = (int(match.group(1)), int(match.group(2)))


def part01(machines):
    tokens = 0
    for machine in machines:
        token_grid = {}
        token_grid[machine.prize] = 0
        q = [machine.prize]
        while len(q) > 0:
            point = q.pop()

            new_point = (point[0] - machine.a[0], point[1] - machine.a[1])
            if (new_point[0] >= 0
                and new_point[0] < machine.prize[0]
                and new_point[1] >= 0
                and new_point[1] < machine.prize[1]
            ):
                if (new_point not in token_grid
                    or token_grid[new_point] > token_grid[point] + 3
                ):
                    token_grid[new_point] = token_grid[point] + 3
                    q.append(new_point)

            new_point = (point[0] - machine.b[0], point[1] - machine.b[1])
            if (new_point[0] >= 0
                and new_point[0] < machine.prize[0]
                and new_point[1] >= 0
                and new_point[1] < machine.prize[1]
            ):
                if (new_point not in token_grid
                    or token_grid[new_point] > token_grid[point] + 1
                ):
                    token_grid[new_point] = token_grid[point] + 1
                    q.append(new_point)
        if (0, 0) in token_grid:
            tokens += token_grid[(0, 0)]
    return tokens


def part02(machines):
    tokens = 0
    for machine in machines:
        px, py = machine.prize
        x1, y1 = machine.a
        x2, y2 = machine.b
        #if (x1 / x2 % 1 == y1 / y2 % 1 == 0
        #    or x2 / x1 % 1 == y2 / y1 % 1 == 0
        #):
        #    a = px / x1
        #    b = px / x2
        #    if b % 1 == 0:
        #        tokens += int(min(a*3, b))
        #else:
        a = (y2*px - x2*py) / (x1*y2 - x2*y1)
        b = (py - a*y1) / y2
        if a % 1 == 0 and b % 1 == 0:
            tokens += int(a)*3 + int(b)
    return tokens


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    filepath = stem + f'.{sys.argv[1]}'
    machines = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 4):
            a_line = lines[i]
            b_line = lines[i+1]
            prize_line = lines[i+2]
            machines.append(Machine(a_line, b_line, prize_line))
    tokens = part02(machines)
    print(tokens)
    offset = 10000000000000
    for i, machine in enumerate(machines):
        machine.prize = (machine.prize[0] + offset, machine.prize[1] + offset)
    tokens = part02(machines)
    print(tokens)
