import sys
import itertools
import re
from common.perf import profiler
from common.io import pretty_print
import cmath

def build_grid(input, threshold):
  file = open(input, 'r')
  temp = {}
  max_x = 0
  max_y = 0
  for line in file.readlines()[2:]:
    match = re.match('^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+).*', line)
    max_x = max(max_x, int(match.group(1)))
    max_y = max(max_y, int(match.group(2)))
    temp[complex(int(match.group(1)), int(match.group(2)))] = tuple(map(int, match.group(3, 4, 5, 6)))
  max_x += 1
  max_y += 1
  grid = {} 
  for i in range(0, max_x):
    for j in range(0, max_y):
      c = complex(i, j)
      if temp[c][1] == 0:
        grid[c] = '_'
        empty = complex(i, j)
      elif temp[c][1] > threshold:
        grid[c] = '#'
      else:
        grid[c] = '.'
  return grid, complex(max_x-1, 0), empty 

def get_adjacent(grid, xy):
  for inc in [complex(0, 1), complex(0, -1), complex(-1, 0), complex(1, 0)]:
    dir = xy + inc 
    if dir not in grid or grid[dir] == '#':
      continue 
    yield dir
  
def get_distances(grid, empty):
  distances = {}
  for c in grid.keys():
    distances[c] = len(grid)
  distances[empty] = 0 
  visited = {empty}
  todo = [empty] 
  while todo:
    current = todo.pop() 
    visited.add(current)
    for dir in get_adjacent(grid, current):
      if dir in visited:
        continue 
      if dir not in distances:
        distances[dir] = 0
      distances[dir] = min(distances[dir], distances[current] + 1)
      todo.append(dir) 
  return distances
   
  
def cprint(grid):
  max_x = 0
  max_y = 0
  for key in grid.keys():
    max_x = max(max_x, key.real) 
    max_y = max(max_y, key.imag)
  max_x = int(max_x) + 1
  max_y = int(max_y) + 1
  output = [['']*max_y for i in range(0, max_x)] 
  for key, value in grid.items():
    output[int(key.real)][int(key.imag)] = value
  pretty_print(output)    

def get_steps(grid, goal, empty):
  cprint(grid)
  distances = get_distances(grid, empty)
  distance_to_empty = distances[goal-complex(1, 0)]
  total_steps = goal.real
  print(distance_to_empty+1+(total_steps-1)*5)
  
    
@profiler
def main(argv):
  grid, goal, empty = build_grid(argv[0], 100)
  get_steps(grid, goal, empty)

if __name__ == "__main__":
  main(sys.argv[1:])
