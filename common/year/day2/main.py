import sys
from common.perf import profiler


def is_safe_1(report):
    first = int(report[0])
    second = int(report[1])
    if first == second:
        return False
    if abs(first - second) > 3:
        return False
    increasing = first < second
    current = second
    safe = True
    for level in report[2:]:
        level = int(level)
        if abs(level - current) > 3:
            safe = False
            break
        if level == current:
            safe = False
            break
        if increasing:
            if level < current:
                safe = False
                break
        else:
            if level > current:
                safe = False
                break
        current = level
    return safe

def is_safe_2(report):
    if is_safe_1(report):
        return True
    for i in range(0, len(report)):
        if is_safe_1(report[0:i]+report[i+1:]):
            return True
    return False

def check_reports(lines):
    part1 = 0
    part2 = 0
    for line in lines:
        report = line.split()
        if is_safe_1(report):
            part1 += 1        
        if is_safe_2(report):
            part2 += 1
        
    print(part1)
    print(part2)


@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    check_reports(file.readlines())


if __name__ == "__main__":
    main(sys.argv[1:])
