import heapq
import math
import sys
from common.perf import profiler
from common.io import pretty_print

def get_grid(size, bytes):
  grid = [ ['.']*size for i in range(size)]
  for x, y in bytes:
    grid[x][y] = '#'
  return grid

def get_neighbors(grid, x, y):
  directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
  for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= len(grid):
      continue
    if ny < 0 or ny >= len(grid[0]):
      continue
    if grid[nx][ny] == '.':
      yield nx, ny

def get_shortest_path(grid):
  ex, ey = len(grid)-1, len(grid[0])-1
  candidates = []
  heapq.heappush(candidates, (0, 0, 0))
  visited = set()
  while candidates:
    distance, x, y = heapq.heappop(candidates)
    if (x, y) in visited:
      continue
    visited.add((x, y))
    if (x, y) == (ex, ey):
      return distance
    for nx, ny in get_neighbors(grid, x, y):
      heapq.heappush(candidates, (distance+1, nx, ny))    
  return None

def part1(size, bytes):
  grid = get_grid(size, bytes)  
  return get_shortest_path(grid)

def part2(size, bytes, count):
  left = count
  right = len(bytes)
  middle = int(math.floor(left+right)/2)
  while right - left > 1:
    grid = get_grid(size, bytes[:middle])    
    if not get_shortest_path(grid):
      right = middle
      middle = int(math.floor(left + middle)/2)
    else:
      left = middle
      middle = int(math.floor(right + middle)/2)    
  res = bytes[middle]
  return res[1], res[0]
  




@profiler
def main(argv):
  input_file = argv[0]
  count = int(argv[1])
  size = int(argv[2])
  file = open(input_file, 'r')
  bytes = []
  for line in file.readlines():
    y, x = line.strip().split(",")
    bytes.append((int(x), int(y)))    
  print(part1(size, bytes[:count]))
  print(part2(size, bytes, count))

if __name__ == "__main__":
  main(sys.argv[1:])
