import heapq
import sys
from common.perf import profiler
from common.io import get_2d_string_input

def get_start_end(grid):
  start = None
  end = None
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 'S':
        start = (i, j)
      elif grid[i][j] == 'E':
        end = (i, j)
        
  return start, end

def get_height(grid, x, y):
  candidate = grid[x][y]
  possible_height = ord(candidate)
  if candidate == 'S':
    possible_height = ord('a')
  elif candidate == 'E':
    possible_height = ord('z')
  return possible_height

def get_neighbors(grid, x, y):
  current_height = get_height(grid, x, y)
  for dir in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    if dir[0] < 0 or dir[0] >= len(grid) or dir[1] < 0 or dir[1] >= len(grid[0]):
      continue    
    possible_height = get_height(grid, dir[0], dir[1])
    if possible_height > current_height + 1:
      continue
    yield dir

def get_neighbors_descending(grid, x, y):
  current_height = get_height(grid, x, y)
  for dir in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    if dir[0] < 0 or dir[0] >= len(grid) or dir[1] < 0 or dir[1] >= len(grid[0]):
      continue    
    possible_height = get_height(grid, dir[0], dir[1])
    if possible_height < current_height - 1:
      continue
    yield dir

def djikstra(grid, sx, sy, ex, ey):
  distances = {}
  heap = []
  heapq.heappush(heap, (0, sx, sy))
  while heap:
    distance, cx, cy = heapq.heappop(heap)    
    if (cx, cy) in distances:
      continue
    distances[(cx, cy)] = distance    
    if (cx, cy) == (ex, ey):
      return distance
    for nx, ny in get_neighbors(grid, cx, cy):
      heapq.heappush(heap, (distance+1, nx, ny))
  return -1

def get_best_distance(grid, ex, ey):
  distances = {}
  best_distance = sys.maxsize
  heap = []
  heapq.heappush(heap, (0, ex, ey))
  while heap:
    distance, cx, cy = heapq.heappop(heap)
    if (cx, cy) in distances:
        continue
    distances[(cx, cy)] = distance
    if grid[cx][cy] in ['a', 'S']:
      if distance < best_distance:
        best_distance = distance
    for nx, ny in get_neighbors_descending(grid, cx, cy):
      if (nx, ny) in distances:
        continue
      heapq.heappush(heap, (distance+1, nx, ny))
  return best_distance

def part1(grid):
  start, end = get_start_end(grid)
  return djikstra(grid, start[0], start[1], end[0], end[1])

def part2(grid):
  _, end = get_start_end(grid)
  return get_best_distance(grid, end[0], end[1])

@profiler
def main(argv):
  input_file = argv[0]
  grid = get_2d_string_input(input_file)
  print(part1(grid))
  print(part2(grid))

if __name__ == "__main__":
  main(sys.argv[1:])
