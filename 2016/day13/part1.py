import sys
from common.perf import profiler


@profiler
def main(argv):
    input = 1364
    target = (31, 39)
    #print(part1(input, target))
    print(part2(input))


def part1(input, target):
    visited = set()
    visited.add((1, 1))
    candidates = [(1, 1, 0)]
    while candidates:
        candidate = candidates.pop(0)
        if candidate[0] == target[0] and candidate[1] == target[1]:
            return candidate[2]
        for neighbor in get_neighbors(candidate[0], candidate[1], input):
            if neighbor in visited:
                continue
            candidates.append((neighbor[0], neighbor[1], candidate[2]+1))
            visited.add((neighbor[0], neighbor[1]))


def part2(input):
    visited = set()
    visited.add((1, 1))
    candidates = [(1, 1, 0)]
    while candidates:
        candidate = candidates.pop(0)        
        for neighbor in get_neighbors(candidate[0], candidate[1], input):
            if neighbor in visited:
                continue
            if candidate[2] < 50:
              candidates.append((neighbor[0], neighbor[1], candidate[2]+1))
              visited.add((neighbor[0], neighbor[1]))
    return len(visited)


def get_neighbors(x, y, input):
    candidates = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    for candidate in candidates:
        if can_visit(candidate[0], candidate[1], input):
            yield candidate


def can_visit(x, y, input):
    if x < 0 or y < 0:
        return False
    value = x*x + 3*x + 2*x*y + y + y*y + input
    return bin(value).count('1') % 2 == 0


if __name__ == "__main__":
    main(sys.argv[1:])
