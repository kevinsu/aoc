import sys
from common.perf import profiler
from common.io import get_2d_string_input as get_input

def get_neighbors(grid, height, i, j):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  for direction in directions:
    new_i = direction[0] + i
    new_j = direction[1] + j
    if new_i < 0 or new_i >= len(grid):
      continue
    if new_j < 0 or new_j >= len(grid[0]):
      continue
    if grid[new_i][new_j] == '.':
      continue
    if int(grid[new_i][new_j]) == height+1:
      yield (new_i, new_j)
    
def part1(grid):
  # Coordinate to set of reachable 9s
  reachable = {}
  for i in range(0, len(grid)):
    reachable[i] = {}
    for j in range(0, len(grid[0])):
      if grid[i][j] == '9':        
        reachable[i][j] = {(i, j)}
  for height in range(8, -1, -1):
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] == '.':
          continue
        current_height = int(grid[i][j])
        if current_height != height:
          continue
        destinations = set()
        for neighbor in get_neighbors(grid, height, i, j):
          destinations.update(reachable.get(neighbor[0], {}).get(neighbor[1], set()))
        reachable[i][j] = destinations
  sum = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == '0':
        sum += len(reachable[i][j])
  return sum

def part2(grid):
  # Coordinate to set of reachable 9s
  reachable = {}
  for i in range(0, len(grid)):
    reachable[i] = {}
    for j in range(0, len(grid[0])):
      if grid[i][j] == '9':        
        reachable[i][j] = 1
  for height in range(8, -1, -1):
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] == '.':
          continue
        current_height = int(grid[i][j])
        if current_height != height:
          continue
        rating = 0
        for neighbor in get_neighbors(grid, height, i, j):
          rating += reachable.get(neighbor[0], {}).get(neighbor[1], 0)          
        reachable[i][j] = rating
  sum = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == '0':
        sum += reachable[i][j]
  return sum


@profiler
def main(argv):
  grid = get_input(argv[0])
  #print(part1(grid))
  print(part2(grid))
  
if __name__ == "__main__":
  main(sys.argv[1:])
