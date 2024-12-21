import heapq
import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input


def get_start_end(grid):
    sx = None
    sy = None
    ex = None
    ey = None
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 'S':
                sx = i
                sy = j
            elif grid[i][j] == 'E':
                ex = i
                ey = j
    return sx, sy, ex, ey


def get_neighbors(grid, x, y):
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= len(grid):
            continue
        if ny < 0 or ny >= len(grid[0]):
            continue
        if grid[nx][ny] in ('.', 'E', 'S'):
            yield nx, ny


def get_cheat_neighbors(grid, x, y, limit=2):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in ('.', 'E'):
                continue
            manhattan = abs(x-i) + abs(y-j)
            if manhattan < 2:
                continue
            if manhattan > limit:
                continue
            yield i, j, manhattan
    
def get_shortest_path_with_map(grid, ex, ey):
    candidates = []
    heapq.heappush(candidates, (0, ex, ey))
    visited = set()
    distance_map = {}
    while candidates:
        distance, x, y = heapq.heappop(candidates)
        if distance_map.get((x, y), sys.maxsize) > distance:
            distance_map[(x, y)] = distance
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in get_neighbors(grid, x, y):
            heapq.heappush(candidates, (distance+1, nx, ny))
    return distance_map

def count_cheats(grid, sx, sy, ex, ey, savings, limit=2):
    candidates = [(sx, sy, 0, {(sx, sy)})]
    visited = set()
    sum = 0
    all_shortest_paths = get_shortest_path_with_map(grid, ex, ey)
    max_distance = all_shortest_paths[(sx, sy)]    
    target = max_distance - savings    
    while candidates:
        x, y, distance, path = candidates.pop(0)        
        if (x, y) in visited:
            continue
        if distance > target:
            continue
        visited.add((x, y))
        if (x, y) == (ex, ey):
            sum += 1
            continue
        for nx, ny in get_neighbors(grid, x, y):
            if (nx, ny) in path:
                continue
            if (nx, ny) in visited:
              continue
            candidates.append((nx, ny, distance+1, path | {(nx, ny)}))        
        for nx, ny, nd in get_cheat_neighbors(grid, x, y, limit=limit):
            if (nx, ny) in path:
              continue
            shortest_path = all_shortest_paths[(nx, ny)]
            new_distance = distance + nd + shortest_path
            if new_distance <= target:
                sum += 1   
    return sum


def part1(grid):
    sx, sy, ex, ey = get_start_end(grid)    
    return count_cheats(grid, sx, sy, ex, ey, 100, limit=20)


@profiler
def main(argv):
    grid = get_input(argv[0])
    sx, sy, ex, ey = get_start_end(grid)    
    print(count_cheats(grid, sx, sy, ex, ey, 100, limit=2))
    print(count_cheats(grid, sx, sy, ex, ey, 100, limit=20))
    

if __name__ == "__main__":
    main(sys.argv[1:])
