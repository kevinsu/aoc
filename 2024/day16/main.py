import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input

import heapq


EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

INCREMENTS = {
  EAST : (0, 1),
  SOUTH : (1, 0),
  WEST : (0, -1),
  NORTH : (-1, 0)
}

def clockwise(direction):
  return (direction - 1) % 4

def counterclockwise(direction):
  return (direction +1) % 4
    
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

def part1(grid):
  sx, sy, ex, ey = get_start_end(grid)
  candidates = []
  heapq.heappush(candidates, (0, sx, sy, EAST))
  visited = set()
  while candidates:    
    candidate = heapq.heappop(candidates)
    score, cx, cy, direction = candidate
    if (cx, cy, direction) in visited:
      continue
    if cx == ex and cy == ey:
      return score
    visited.add((cx, cy, direction))    
    heapq.heappush(candidates, (score + 1000, cx, cy, clockwise(direction)))    
    heapq.heappush(candidates, (score + 1000, cx, cy, counterclockwise(direction)))        
    dx, dy = INCREMENTS[direction]
    nx = cx + dx
    ny = cy + dy
    if grid[nx][ny] == '#':
      continue
    heapq.heappush(candidates, (score+1, nx, ny, direction))      
  return sys.maxsize

def part2(grid, lowest_score):
  sx, sy, ex, ey = get_start_end(grid)
  candidates = [(sx, sy, EAST, 0, [(sx, sy)])]  
  visited = {}
  best_squares = set()
  while candidates:
    x, y, direction, score, path = candidates.pop(0)
    if score > lowest_score:
      continue
    if x == ex and y == ey:      
      best_squares.update(path)      
      continue
    if (x, y, direction) in visited:
      if score > visited[(x, y, direction)]:
        continue
    visited[(x, y, direction)] = score
    candidates.append((x, y, clockwise(direction), score+1000, path))
    candidates.append((x, y, counterclockwise(direction), score+1000, path))
    dx, dy = INCREMENTS[direction]
    nx = x + dx
    ny = y + dy
    if grid[nx][ny] == '#':
      continue
    candidates.append((nx, ny, direction, score+1, path + [(nx, ny)]))      
  return len(best_squares)

@profiler
def main(argv):
  grid = get_input(argv[0])
  best_score = part1(grid)
  print(best_score)
  print(part2(grid, best_score))

if __name__ == "__main__":
  main(sys.argv[1:])
