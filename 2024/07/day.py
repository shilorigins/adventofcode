import sys


class Equation:
    def __init__(self, string):
        test_value, nums = string.split(": ")
        self.test_value = int(test_value)
        self.nums = (int(num) for num in nums.split())
        self.operators = []


class Solution:
    def __init__(self, string=None):
        if string:
            self.parse_string(string)

    def parse_string(self, string):
        test_value, nums = string.split(": ")
        self.test_value = int(test_value)
        self.nums = [int(num) for num in reversed(nums.split())]
        self.running_total = self.nums.pop()
        self.string = string

    def copy(self):
        new = Solution()
        new.test_value = self.test_value
        new.nums = self.nums.copy()
        new.running_total = self.running_total
        new.string = self.string
        return new


def part01(equations):
    valid = set()
    q = [Solution(equation) for equation in equations]
    while len(q) > 0:
        solution = q.pop()
        if len(solution.nums) > 0:
            new_add = solution.copy()
            new_add.running_total += new_add.nums.pop()
            q.append(new_add)
            new_multiply = solution.copy()
            new_multiply.running_total *= new_multiply.nums.pop()
            q.append(new_multiply)
        elif solution.running_total == solution.test_value:
            valid.add(solution.string)
    return valid


def part02(equations):
    valid = set()
    q = [Solution(equation) for equation in equations]
    while len(q) > 0:
        solution = q.pop()
        if len(solution.nums) > 0:
            new_add = solution.copy()
            new_add.running_total += new_add.nums.pop()
            q.append(new_add)
            new_multiply = solution.copy()
            new_multiply.running_total *= new_multiply.nums.pop()
            q.append(new_multiply)
            new_concat = solution.copy()
            new_concat.running_total = int(str(new_concat.running_total) + str(new_concat.nums.pop()))
            q.append(new_concat)
        elif solution.running_total == solution.test_value:
            valid.add(solution.string)
    return valid


if __name__ == "__main__":
    match sys.argv[1]:
        case "test":
            filepath = "07.test"
        case "input":
            filepath = "07.input"
    with open(filepath) as f:
        equations = f.read().strip().split('\n')
    valid_equations = part01(equations)
    print(sum([int(eq.split(':')[0]) for eq in valid_equations]))
    valid_equations = part02(equations)
    print(sum([int(eq.split(':')[0]) for eq in valid_equations]))
