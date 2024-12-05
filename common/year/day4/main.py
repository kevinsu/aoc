import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input
from common.io import pretty_print

DIRECTIONS = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1)
]

def is_xmas(input, x, y, inc_x, inc_y):
    if x + 3*inc_x < 0 or x + 3*inc_x >= len(input):
        return False
    if y + 3*inc_y < 0 or y + 3*inc_y >= len(input[0]):
        return False
    if input[x + inc_x][y + inc_y] != 'M':
        return False
    if input[x + 2*inc_x][y + 2*inc_y] != 'A':
        return False
    if input[x + 3*inc_x][y + 3*inc_y] != 'S':
        return False
    return True

def part1(input):
    count = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            current = input[i][j]
            if current != 'X':
                continue
            for direction in DIRECTIONS:
                if is_xmas(input, i, j, direction[0], direction[1]):
                    count += 1
    return count

def is_cross(input, x, y):
    if input[x+1][y+1] != 'A':
        return False
    if input[x][y] not in ['M', 'S']:
        return False
    if input[x][y+2] not in ['M', 'S']:
        return False
    if input[x+2][y] not in ['M', 'S']:
        return False
    if input[x+2][y+2] not in ['M', 'S']:
        return False
    if input[x][y] == input[x+2][y+2]:
        return False
    if input[x+2][y] == input[x][y+2]:
        return False
    return True

def part2(input):
    count = 0
    for i in range(0, len(input)-2):
        for j in range(0, len(input[0])-2):
            if is_cross(input, i, j):
                count += 1
    return count

@profiler
def main(argv):
    input = get_input(argv[0])
    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main(sys.argv[1:])
