import sys
from common.io import pretty_print, get_2d_string_input as get_input

def get_start(input):
  for j, cell in enumerate(input[0]):
    if cell == '.':
      return 0, j

def get_end(input):
  for j, cell in enumerate(input[len(input)-1]):
    if cell == '.':
      return len(input)-1, j

# Don't have to check borders cause it's all # or start/end
def get_adjacent(input, i, j):
  cell = input[i][j]
  if cell == '>':
    return [(i, j+1)]
  elif cell == '<':
    return [(i, j-1)]
  elif cell == '^':
    return [(i-1, j)]
  elif cell == 'v':
    return [(i+1, j)]
  adjacent = []
  if input[i-1][j] != '#':
    adjacent.append((i-1, j))
  if input[i+1][j] != '#':
    adjacent.append((i+1, j))
  if input[i][j-1] != '#':
    adjacent.append((i, j-1))
  if input[i][j+1] != '#':
    adjacent.append((i, j+1))
  return adjacent

def get_longest(input, start_x, start_y, end_x, end_y):
  todo = [(start_x, start_y, {(start_x, start_y)})]
  paths = []
  counter = 0
  while todo:
    counter += 1
    if counter % 1000 == 0:
      print(counter)
    current_x, current_y, current_visited = todo.pop()
    for next_x, next_y in get_adjacent(input, current_x, current_y):
      if (next_x, next_y) in current_visited:
        continue
      next_visited = current_visited.copy()
      next_visited.add((next_x, next_y))
      if (next_x, next_y) == (end_x, end_y):
        paths.append(next_visited)
        continue
      todo.append((next_x, next_y, next_visited))
  max_length = 0
  for visited in paths:
    max_length = max(max_length, len(visited))
  return max_length-1
     
def main(argv):
  input = get_input(argv[0])
  pretty_print(input)
  start = get_start(input)
  end = get_end(input)
  print(start, end)
  print(get_longest(input, *start, *end))

if __name__ == "__main__":
  main(sys.argv[1:])
