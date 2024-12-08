import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input
from common.io import pretty_print

from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


DIRECTIONS = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


def get_next_location(current_location, current_heading):
    direction = DIRECTIONS[current_heading]
    return (current_location[0] + direction[0], current_location[1] + direction[1])


def part1(grid):
    start = None
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] == '^':
                start = (x, y)
                break
    current_heading = 0
    current_location = start
    visited = {start}
    while (True):
        next_location = get_next_location(current_location, current_heading)
        if next_location[0] < 0 or next_location[0] >= len(grid) or next_location[1] < 0 or next_location[1] >= len(grid[0]):
            break
        if grid[next_location[0]][next_location[1]] == '#':
            current_heading = (current_heading + 1) % 4            
            continue
        visited.add(next_location)        
        current_location = next_location
    return len(visited)

def has_cycle(grid, start, new_x, new_y):
    visited = {(start[0], start[1], 0)}
    current_heading = 0
    current_location = start
    while True:
        next_location = get_next_location(current_location, current_heading)
        if next_location[0] < 0 or next_location[0] >= len(grid) or next_location[1] < 0 or next_location[1] >= len(grid[0]):
            break
        if (next_location[0], next_location[1], current_heading) in visited:            
            return True
        if grid[next_location[0]][next_location[1]] == '#' or next_location == (new_x, new_y):
            current_heading = (current_heading +1) % 4
            continue
        visited.add((next_location[0], next_location[1], current_heading))        
        current_location = next_location
    return False

def part2(grid):
    start = None
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] == '^':
                start = (x, y)
                break
    current_heading = 0
    current_location = start
    visited = {start}
    while (True):
        next_location = get_next_location(current_location, current_heading)
        if next_location[0] < 0 or next_location[0] >= len(grid) or next_location[1] < 0 or next_location[1] >= len(grid[0]):
            break
        if grid[next_location[0]][next_location[1]] == '#':
            current_heading = (current_heading + 1) % 4            
            continue
        visited.add(next_location)        
        current_location = next_location
    count = 0
    i = 0
    for candidate in visited:
        if has_cycle(grid, start, candidate[0], candidate[1]):
            count += 1
    return count
    
@profiler
def main(argv):
    grid = get_input(argv[0])
    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main(sys.argv[1:])
