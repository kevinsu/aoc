import functools
import sys
from common.perf import profiler
from itertools import combinations


def get_middle(rules, update):
    for combo in combinations(update, 2):
        left = combo[0]
        right = combo[1]
        if f'{right}|{left}' in rules:
            return 0
    return int(update[int(len(update)/2)])


def part1(rules, updates):
    sum = 0
    for update in updates:
        sum += get_middle(rules, update)
    return sum


def make_comparator(rules):
    def compare(x, y):
        if f'{x}|{y}' in rules:
            return -1
        return 1
    return compare


def get_middle_sorted(rules, update):
    new_update = sorted(update, key=functools.cmp_to_key(make_comparator(rules)))
    if new_update == update:
        return 0
    return int(new_update[int(len(new_update)/2)])


def part2(rules, updates):
    sum = 0
    for update in updates:
        sum += get_middle_sorted(rules, update)
    return sum


@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    rules = set()
    done_with_rules = False
    updates = []
    for line in file.readlines():
        if line == '\n':
            done_with_rules = True
            continue
        if done_with_rules:
            updates.append(line.strip().split(","))
        else:
            rules.add(line.strip())
    print(part1(rules, updates))
    print(part2(rules, updates))


if __name__ == "__main__":
    main(sys.argv[1:])
