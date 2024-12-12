from itertools import pairwise
import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input


def get_fill(grid, region_name, region_name_map, visited, i, j, region):
    if (i, j) in visited:
        return region
    visited.add((i, j))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    letter = grid[i][j]
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if (new_i, new_j) in visited:
            continue
        if new_i < 0 or new_i >= len(grid):
            continue
        if new_j < 0 or new_j >= len(grid[0]):
            continue
        next_letter = grid[new_i][new_j]
        if next_letter != letter:
            continue
        region.add((new_i, new_j))
        region_name_map[(new_i, new_j)] = region_name
        get_fill(grid, region_name, region_name_map,
                 visited, new_i, new_j, region)


def update_perimeter_map(i, j, region_name_map, perimeter_map):
    region_name = region_name_map[(i, j)]
    if region_name not in perimeter_map:
        perimeter_map[region_name] = 0
    perimeter_map[region_name] += 1


def update_fences(i, j, x, y, region_name, fences, first=True):
    if region_name not in fences:
        fences[region_name] = set()
    fences[region_name].add((i, j, first))


def update_perimeter(grid, i, j, x, y, region_name_map, perimeter_map, fences):
    if i < 0 or j < 0:
        update_perimeter_map(x, y, region_name_map, perimeter_map)
        region_name = region_name_map[(x, y)]
        update_fences(i, j, x, y, region_name, fences, first=False)
        return
    if x == len(grid) or y == len(grid):
        update_perimeter_map(i, j, region_name_map, perimeter_map)
        region_name = region_name_map[(i, j)]
        update_fences(i, j, x, y, region_name, fences, first=True)
        return

    if grid[i][j] == grid[x][y]:
        return
    update_perimeter_map(x, y, region_name_map, perimeter_map)
    update_perimeter_map(i, j, region_name_map, perimeter_map)
    update_fences(i, j, x, y, region_name_map[(i, j)], fences, first=True)
    update_fences(i, j, x, y, region_name_map[(x, y)], fences, first=False)


def is_adjacent(f1, f2, horizontal=True):
    if f1[2] != f2[2]:
        return False
    if horizontal and f1[0] != f2[0]:
        return False
    elif not horizontal and f1[1] != f2[1]:
        return False
    return (abs(f1[0]-f2[0]) + abs(f1[1]-f2[1])) == 1


def update_adjacent(perimeter_map, fences, horizontal=True):
    for region_name, fence in fences.items():
        sorted_fences = None
        if horizontal:
            sorted_fences = sorted(fence, key=lambda x: x[0]*1000+x[1])
        else:
            sorted_fences = sorted(fence, key=lambda x: x[1]*1000+x[0])
        for f1, f2 in pairwise(sorted_fences):
            if is_adjacent(f1, f2, horizontal=horizontal):
                perimeter_map[region_name] -= 1


def get_perimeter(grid, region_name_map):
    perimeter_map = {}
    horizontal_fences = {}
    vertical_fences = {}
    # Scan horizontal
    for i in range(0, len(grid)+1):
        for j in range(0, len(grid[0])):
            update_perimeter(grid, i-1, j, i, j, region_name_map,
                             perimeter_map, horizontal_fences)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])+1):
            update_perimeter(grid, i, j-1, i, j, region_name_map,
                             perimeter_map, vertical_fences)
    side_map = perimeter_map.copy()
    update_adjacent(side_map, horizontal_fences)
    update_adjacent(side_map, vertical_fences, horizontal=False)
    return perimeter_map, side_map


def get_region(grid, region_name_map, visited, i, j):
    letter = grid[i][j]
    region_name = f'{letter},{i},{j}'
    region = {(i, j)}
    region_name_map[(i, j)] = region_name
    get_fill(grid, region_name, region_name_map, visited, i, j, region)
    return region_name, region


def solve(grid):
    regions = {}
    region_name_map = {}
    visited = set()
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (i, j) in visited:
                continue
            region_name, current_region = get_region(
                grid, region_name_map, visited, i, j)
            regions[region_name] = current_region
    perimeter_map, side_map = get_perimeter(grid, region_name_map)
    part1 = 0
    for key in regions.keys():
        part1 += len(regions[key]) * perimeter_map[key]
    part2 = 0
    for key in regions.keys():
        part2 += len(regions[key]) * side_map[key]
    print('Part 1: ', part1)
    print('Part 2: ', part2)
    

@profiler
def main(argv):
    grid = get_input(argv[0])
    solve(grid)


if __name__ == "__main__":
    main(sys.argv[1:])
