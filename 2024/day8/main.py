import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input
from itertools import combinations


def get_antinodes(grid, n1, n2):
    a1 = (n1[0] - (n2[0]-n1[0]), n1[1] - (n2[1]-n1[1]))
    a2 = (n2[0] + (n2[0]-n1[0]), n2[1] + (n2[1]-n1[1]))
    if a1[0] >= 0 and a1[0] < len(grid) and a1[1] >= 0 and a1[1] < len(grid[0]):
        yield a1
    if a2[0] >= 0 and a2[0] < len(grid) and a2[1] >= 0 and a2[1] < len(grid[0]):
        yield a2


def part1(grid):
    antennae = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            node = grid[i][j]
            if node == '.':
                continue
            if node not in antennae:
                antennae[node] = []
            antennae[node].append((int(i), int(j)))
    antinodes = set()
    for freq, nodes in antennae.items():
        for n1, n2 in combinations(nodes, 2):
            for antinode in get_antinodes(grid, n1, n2):
                antinodes.add(antinode)
    return len(antinodes)


def get_antinodes_line(grid, n1, n2):
    yield n1
    yield n2
    difference = (n2[0]-n1[0], n2[1]-n1[1])
    antinode = n1
    while True:
        antinode = (antinode[0]-difference[0], antinode[1] - difference[1])
        if antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid[0]):
            yield antinode
        else:
            break
    antinode = n2
    while True:
        antinode = (antinode[0]+difference[0], antinode[1] + difference[1])
        if antinode[0] >= 0 and antinode[0] < len(grid) and antinode[1] >= 0 and antinode[1] < len(grid[0]):
            yield antinode
        else:
            break


def part2(grid):
    antennae = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            node = grid[i][j]
            if node == '.':
                continue
            if node not in antennae:
                antennae[node] = []
            antennae[node].append((int(i), int(j)))
    antinodes = set()
    for nodes in antennae.values():
        for n1, n2 in combinations(nodes, 2):
            for antinode in get_antinodes_line(grid, n1, n2):
                antinodes.add(antinode)
    return len(antinodes)


@profiler
def main(argv):
    input = get_input(argv[0])
    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main(sys.argv[1:])
