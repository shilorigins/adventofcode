#filepath = "01.test"
filepath = "01.input"


def part01():
    password = 0
    pointer = 50
    rotations = []
    with open(filepath) as f:
        rotations = f.read().split('\n')[:-1]
    for rotation in rotations:
        step = int(rotation[1:])
        if rotation.startswith('L'):
            step = -step
        pointer = (pointer + step) % 100
        if pointer == 0:
            password += 1
    return password


def part02():
    password = 0
    pointer = 50
    rotations = []
    with open(filepath) as f:
        rotations = f.read().split('\n')[:-1]
    for rotation in rotations:
        step = int(rotation[1:])
        if rotation.startswith('L'):
            step = -step
        password += abs((pointer + step) // 100)
        pointer = (pointer + step) % 100
    return password


if __name__ == "__main__":
    print(part01())
    print(part02())
