import heapq
import sys
from common.io import get_2d_string_input, pretty_print

def display(grid):
  for row in grid:
    print(' '.join(list(map(str, row))))
  print()

def get_shortest_paths(grid, x, y):
  distances = [[sys.maxsize]*len(grid[0]) for x in grid]
  distances[x][y] = 0
  unvisited = []
  for i, row in enumerate(grid):
    for j, cell in enumerate(row):
      if cell != '#':
        heapq.heappush(unvisited, (sys.maxsize, i, j))  
  heapq.heappush(unvisited, (0, x, y))
  visited = set()
  while unvisited:
    current_distance, current_x, current_y = heapq.heappop(unvisited)
    if (current_x, current_y) in visited:
      continue
    visited.add((current_x, current_y))
    for next_x, next_y in get_neighbors(grid, current_x, current_y):
      if (next_x, next_y) in visited:
        continue 
      tentative = distances[current_x][current_y] + 1
      if tentative < distances[next_x][next_y]:
        distances[next_x][next_y] = tentative 
        heapq.heappush(unvisited, (tentative, next_x, next_y))
  return distances

def get_neighbors(grid, x, y):
  for dir in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    if dir[0] < 0 or dir[0] >= len(grid) or dir[1] < 0 or dir[1] >= len(grid[0]):
      continue
    if grid[dir[0]][dir[1]] == '#':
      continue
    yield dir
    
