from math import floor
import sys
from common.perf import profiler
from common.io import pretty_print
from common.loop import CycleFinder

ROCK_TYPES = {
  0 : {(0, 0), (0, 1), (0, 2), (0, 3)},
  1 : {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
  2 : {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)},
  3 : {(0, 0), (1, 0), (2, 0), (3, 0)},
  4 : {(0, 0), (0, 1), (1, 0), (1, 1)}
}

def pp(grid):
  pretty_print(reversed(grid))

class Rock:
  def __init__(self, x, y, rock_type):
    self.x = x
    self.y = y
    self.tiles = ROCK_TYPES[rock_type]
  
  def get_left_tiles(self):
    for tile in self.tiles:
      if (tile[0], tile[1]-1) not in self.tiles:
        yield (tile[0] + self.x, tile[1] + self.y)    
    
  def get_right_tiles(self):
    for tile in self.tiles:
      if (tile[0], tile[1]+1) not in self.tiles:
        yield (tile[0] + self.x, tile[1] + self.y)    

  def get_below_tiles(self):
    for tile in self.tiles:
      if (tile[0]-1, tile[1]) not in self.tiles:
        yield (tile[0] + self.x, tile[1] + self.y)    
    
  def get_tiles(self):
    return [(x+self.x, y+self.y) for x, y in self.tiles]

  def blow(self, grid, direction):
    if direction == '<':
      for left_tile in self.get_left_tiles():
        if left_tile[1] == 0:
          return
        if grid[left_tile[0]][left_tile[1]-1] != '.':
          return
      self.y -= 1
    else:
      for right_tile in self.get_right_tiles():        
        if right_tile[1] == len(grid[0])-1:
          return
        if grid[right_tile[0]][right_tile[1]+1] != '.':
          return
      self.y += 1
  
  def drop(self, grid):
    for below_tile in self.get_below_tiles():
      if below_tile[0] == 0:
        return False
      if grid[below_tile[0]-1][below_tile[1]] != '.':
        return False
    self.x -= 1
    return True

  def settle(self, grid):
    new_top = 0
    for tile in self.get_tiles():
      grid[tile[0]][tile[1]] = '#'
      new_top = max(new_top, tile[0])
    return new_top + 1
    
def get_grid_state(grid, pattern, count, pattern_index):
  return f'{count%5} {pattern_index % len(pattern)} {"".join(["".join(row) for row in grid[-50:-6]])}'

GOAL = 1000000000000
def get_height(cycle_heights, cycle_start, cycle_height, count, current_height):
  cycle_length = count - cycle_start + 1
  multiplier = (GOAL - current_height) / cycle_length
  remainder = (GOAL - current_height) % cycle_length
  return current_height + cycle_height * multiplier + cycle_heights[remainder]

# Find the first repeat and mark it as the start of the cycle.  
# Until we see the repeat again, save the count and height
# When we see the repeat for the second time, break.
def part1(pattern, total_rocks):
  grid = [['.'] * 7]
  count = 0
  top_of_rocks = 0
  pattern_index = 0
  visited = {}
  cycle_finder = CycleFinder()
  previous = 0
  
  while count < total_rocks:
    spawn_height = top_of_rocks + 7
    if len(grid) < spawn_height:
      grid.extend([['.'] * 7 for i in range(spawn_height-len(grid))])      
    grid_state = get_grid_state(grid, pattern, count, pattern_index)
    if cycle_finder.find_cycle(grid_state, count, top_of_rocks):
      break
    if count % 1720 == 5:
      print(top_of_rocks-previous, count)
      previous = top_of_rocks
    visited[grid_state] = count, top_of_rocks   
    rock = Rock(top_of_rocks+3, 2, count%5)
    can_drop = True
    while can_drop:
      rock.blow(grid, pattern[pattern_index % len(pattern)])
      can_drop = rock.drop(grid)
      pattern_index += 1
    new_top = rock.settle(grid)
    top_of_rocks = max(top_of_rocks, new_top)
    count += 1    
  print(top_of_rocks)
  print(cycle_finder.calculate_step(GOAL))
    

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  pattern = file.readline()  
  print(part1(pattern, 20000))  

if __name__ == "__main__":
  main(sys.argv[1:])
