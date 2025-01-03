import math
import re
import sys
from common.perf import profiler

def get_fn(expr):
    if '+' in expr:
        _, right = expr.split('+')
        return lambda x: x + int(right.strip())
    elif '*' in expr:
        _, right = expr.split('*')
        if right.strip() == 'old':
            return lambda x: x * x
        else:
            return lambda x: x * int(right.strip())
    return NotImplementedError


class Monkey:
    def __init__(self, id, items, fn, divisor, true_id, false_id):
        self.id = id
        self.items = items
        self.fn = fn
        self.divisor = divisor
        self.true_id = true_id
        self.false_id = false_id
        self.inspections = 0

    def turn(self, monkeys, gcd, part1=True):
        for item in self.items:
            self.inspections += 1
            worry_level = self.fn(item)
            if part1:
              worry_level = math.floor(worry_level/3)
            worry_level = worry_level % gcd
            if worry_level % self.divisor == 0:
                monkeys[self.true_id].items.append(worry_level)
            else:
                monkeys[self.false_id].items.append(worry_level)
        self.items.clear()


def part1(monkeys, loops, part1=True):
    gcd = 1
    for monkey in monkeys:
        gcd *= monkey.divisor
    for _ in range(1, loops+1):
        for monkey in monkeys:
            monkey.turn(monkeys, gcd, part1=part1)        
    return math.prod(sorted(map(lambda m: m.inspections, monkeys), reverse=True)[:2])


@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    blocks = file.read().split('\n\n')
    monkeys = []
    for block in blocks:
        match = re.match(
            'Monkey\s(\d+):[\s\S]*:\s(.*)\s*Operation: new = (.*)\s*Test: divisible by (\d+)[\s\S]*monkey (\d+)[\s\S]*monkey (\d+)', block)
        id, raw_list, raw_lambda, divisor, true_id, false_id = int(match.group(1)), match.group(
            2), match.group(3), int(match.group(4)), int(match.group(5)), int(match.group(6))
        monkey = Monkey(id, list(map(int, raw_list.split(","))), get_fn(
            raw_lambda), divisor, true_id, false_id)
        monkeys.append(monkey)
    print(part1(monkeys, 20))
    print(part1(monkeys, 10000, False))


if __name__ == "__main__":
    main(sys.argv[1:])
