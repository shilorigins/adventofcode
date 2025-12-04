#filepath = "01.test"
filepath = "01.input"


def part01(rotations):
    password = 0
    pointer = 50
    for step in rotations:
        pointer = (pointer + step) % 100
        if pointer == 0:
            password += 1
    return password


def part02(rotations):
    password = 0
    pointer = 50
    for step in rotations:
        print("Step: ", step)
        password += abs(step) // 100
        if step < 0 and abs(step) < pointer:
            pointer = (pointer + step) % 100
        else:
            pointer += step % 100
            password += pointer // 100
            pointer %= 100
        print("Pointer: ", pointer)
        print("Password: ", password)
        print("\n")
    return password


if __name__ == "__main__":
    with open(filepath) as f:
        rotations = [
            int(rotation[1:]) if rotation.startswith('R') else -int(rotation[1:]) for rotation in f.read().split('\n')[:-1]
        ]
    print("Part 01: ", part01(rotations))
    print("Part 02: ", part02(rotations))
