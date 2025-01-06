import sys


def parse_input(filepath):
    rules = []
    updates = []
    with open(sys.argv[1]) as f:
        rule_text, update_text = f.read().split('\n\n')
        for rule in rule_text.split():
            left, right = rule.split('|')
            rules.append((int(left), int(right)))
        for update in update_text.split():
            updates.append([int(i) for i in update.split(',')])
    return rules, updates


def part01(rules, updates):
    predecessors = {i: set() for i in range(1, 101)}
    for predecessor, successor in rules:
        predecessors[successor].add(predecessor)
    correct_mask = [0 for i in range(len(updates))]
    for i, update in enumerate(updates):
        try:
            required_predecessors = set()
            for num in update:
                if num in required_predecessors:
                    raise ValueError
                else:
                    required_predecessors |= predecessors[num]
            correct_mask[i] = 1
        except ValueError:
            pass
    return correct_mask


def insert_num(update, num, predecessors):
    index = len(update)
    required_predecessors = [set()]
    for i in range(index):
        required_predecessors.append(required_predecessors[i] | predecessors[update[i]])
    while num in required_predecessors[index]:
        index -= 1
    update.insert(index, num)


def part02(rules, updates):
    predecessors = {i: set() for i in range(1, 101)}
    for predecessor, successor in rules:
        predecessors[successor].add(predecessor)
    reordered = []
    for update in updates:
        in_order = []
        for num in update:
            insert_num(in_order, num, predecessors)
        reordered.append(in_order)
    return reordered


if __name__ == "__main__":
    rules, updates = parse_input(sys.argv[1])
    correct_mask = part01(rules, updates)
    print(sum([updates[i][len(updates[i]) // 2] for i in range(len(correct_mask)) if correct_mask[i]]))
    incorrect_updates = [updates[i] for i in range(len(correct_mask)) if not correct_mask[i]]
    reordered = part02(rules, incorrect_updates)
    print(sum([update[len(update) // 2] for update in reordered]))
