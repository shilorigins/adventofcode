import sys
from collections import defaultdict


def part01(reports):
    num_safe = 0
    for report in reports:
        try:
            for i in range(len(report) - 1):
                diff = report[i + 1] - report[i]
                if diff <= 0 or diff > 3:
                    raise ValueError
            num_safe += 1
        except ValueError:
            pass
    print(num_safe)


def is_safe_with_tolerance(report):
    window_fixes = []
    for i in range(len(report) - 2):
        indices_to_remove = set()
        left_diff = report[i + 1] - report[i]
        left_bad = left_diff <= 0 or left_diff > 3
        right_diff = report[i + 2] - report[i + 1]
        right_bad = right_diff <= 0 or right_diff > 3
        ends_diff = report[i + 2] - report[i]
        ends_bad = ends_diff <= 0 or ends_diff > 3
        if not left_bad:
            indices_to_remove.add(i+2)
        if not right_bad:
            indices_to_remove.add(i)
        if not ends_bad:
            indices_to_remove.add(i+1)
        if left_bad or right_bad:
            window_fixes.append(indices_to_remove)
    print(report, file=sys.stderr)
    print(window_fixes, file=sys.stderr)
    is_safe = False
    if len(window_fixes) > 0:
        common_fixes = window_fixes[0].intersection(*window_fixes[1:])
        is_safe = len(common_fixes) > 0
    else:
        is_safe = True
    print(f"Safe = {is_safe}", file=sys.stderr)
    print("", file=sys.stderr)
    return is_safe


def _is_safe_with_tolerance(report):
    bad_count = defaultdict(int)
    for i in range(len(report) - 2):
        left_diff = report[i + 1] - report[i]
        left_bad = left_diff <= 0 or left_diff > 3
        right_diff = report[i + 2] - report[i + 1]
        right_bad = right_diff <= 0 or right_diff > 3
        ends_diff = report[i + 2] - report[i]
        ends_bad = ends_diff <= 0 or ends_diff > 3
        if left_bad:
            bad_count[i] += 1
            bad_count[i+1] += 1
        if right_bad:
            bad_count[i+1] += 1
            bad_count[i+2] += 1
        if ends_bad:
            bad_count[i] += 1
            bad_count[i+2] += 1
    bad_count[0] += 1
    #bad_count[1] += 1
    bad_count[len(report) - 2] += 1
    #bad_count[len(report) - 1] += 1
    num_bad_indices = len([i for i in bad_count.values() if i >= 3])
    print(report, file=sys.stderr)
    print([bad_count[i] for i in range(len(report))], file=sys.stderr)
    print(f"Safe = {num_bad_indices <= 1}", file=sys.stderr)
    print("", file=sys.stderr)
    return num_bad_indices <= 1


def naive(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff <= 0 or diff > 3:
            raise ValueError
    num_safe += 1


def part02(reports):
    safe_reports = []
    unsafe_reports = []
    num_safe = 0
    for report in reports:
        if is_safe_with_tolerance(report):
            safe_reports.append(report)
            num_safe += 1
        else:
            unsafe_reports.append(report)
    with open("02.safe", 'w') as f:
        for report in safe_reports:
            print(report, file=f)
    with open("02.unsafe", 'w') as f:
        for report in unsafe_reports:
            print(report, file=f)
    print(num_safe)

    
if __name__ == "__main__":
    try:
        reports = []
        with open(sys.argv[1]) as f:
            for line in f.readlines():
                report = [int(c) for c in line.split()]
                if report[0] > report[-1]:
                    report = tuple(reversed(report)) 
                reports.append(report)
        #part01(reports)
        part02(reports)
    except FileNotFoundError:
        report = [int(i) for i in sys.argv[1:]]
        #part01([report])
        part02([report])
