import sys
from common.io import pretty_print, get_2d_string_input as get_input
from common.perf import profiler

def get_start(input):
  for j, cell in enumerate(input[0]):
    if cell == '.':
      return 0, j

def get_end(input):
  for j, cell in enumerate(input[len(input)-1]):
    if cell == '.':
      return len(input)-1, j

def get_splits(input, i, j):
  visited = {(i, j)}
  splits = []
  for next_x, next_y in get_adjacent(input, i, j, {}):
    next_cell = (next_x, next_y) 
    next_visited = visited.copy()    
    next_visited.add(next_cell)
    next_next = get_adjacent(input, *next_cell, next_visited)
    while len(next_next) == 1:
      next_cell = next_next[0]
      next_visited.add(next_cell)
      next_next = get_adjacent(input, *next_cell, next_visited)    
    splits.append((next_cell[0], next_cell[1], len(next_visited)-1))
  return splits 

def get_adjacent(input, i, j, visited):
  cell = input[i][j]
  adjacent = []
  if i-1>=0 and input[i-1][j] != '#' and (i-1, j) not in visited:
    adjacent.append((i-1, j))
  if i+1<len(input) and input[i+1][j] != '#' and (i+1, j) not in visited:
    adjacent.append((i+1, j))
  if j-1>=0 and input[i][j-1] != '#' and (i, j-1) not in visited:
    adjacent.append((i, j-1))
  if j+1<len(input[0]) and input[i][j+1] != '#' and (i, j+1) not in visited:
    adjacent.append((i, j+1))
  return adjacent

@profiler
def get_longest(splits, start_x, start_y, end_x, end_y):
  max_distance = 0
  todo = [(start_x, start_y, 0, {(start_x, start_y)})]
  max_length = 0

  while todo:
    current_x, current_y, current_distance, current_visited = todo.pop()
    if (current_x, current_y) == (end_x, end_y):
      if current_distance > max_distance:
        max_distance = current_distance
        max_length = len(current_visited)
        print(max_distance) 
        continue 
    for next_x, next_y, next_distance in splits[(current_x, current_y)]: 
      if (next_x, next_y) in current_visited:
        continue
      todo.append((next_x, next_y, current_distance + next_distance, current_visited|{(next_x, next_y)})) 
  return max_distance

@profiler
def build_splits(input):
  splits = {}
  for i, row in enumerate(input): 
    for j, cell in enumerate(row):
      if cell == '#':
        continue
      adjacent = get_adjacent(input, i, j, {})
      if len(get_adjacent(input, i, j, {})) in [1, 3, 4] :
        splits[(i, j)] = get_splits(input, i, j) 
  return splits

def main(argv):
  input = get_input(argv[0])
  start = get_start(input)
  end = get_end(input)
  print(start, end)
  splits = build_splits(input)
  print(len(splits))
  count = 0
  print(get_longest(splits, *start, *end))

if __name__ == "__main__":
  main(sys.argv[1:])
