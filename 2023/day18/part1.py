import sys
import re
import common.io as io

class Segment():
  def __init__(self, x1, y1, x2, y2, color):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.color = color

  def __str__(self):
    return '(%d, %d)->(%d, %d): %s' % (self.x1, self.y1, self.x2, self.y2, self.color)

def get_instructions(input):
  instructions = []
  file = open(input, 'r')
  for line in file.readlines():
    match = re.match('^(\w)\s(\d+)\s\((.*)\)', line)  
    direction = match.group(1)
    length = int(match.group(2)) 
    color = match.group(3)
    instructions.append((direction, length, color))
  return instructions

def get_segments(instructions):
  min_x = 0
  min_y = 0
  max_x = 0
  max_y = 0
  x1 = 0
  y1 = 0
  x2 = 0
  y2 = 0
  segments = []
  for direction, length, color in instructions:
    if direction == 'R':
      y2 = y1 + length
    elif direction == 'L':
      y2 = y1 - length
    elif direction == 'D':
      x2 = x1 + length
    elif direction == 'U':
      x2 = x1 - length
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)
    min_x = min(min_x, x2)
    min_y = min(min_y, y2)
    segments.append(Segment(x1, y1, x2, y2, color)) 
    x1 = x2
    y1 = y2
  return min_x, min_y, max_x, max_y, segments
     
def build_grid(min_x, min_y, max_x, max_y, segments):
  print(min_x, min_y, max_x, max_y)
  grid = [['.']*(max_y-min_y+1) for i in range(min_x, max_x+1)]
  for segment in segments:
    if segment.x1 != segment.x2:
      increment = 1 if segment.x1 < segment.x2 else -1
      for i in range(segment.x1, segment.x2+increment, increment):
        grid[i-min_x][segment.y1-min_y] = '#'
    else:
      increment = 1 if segment.y1 < segment.y2 else -1
      for j in range(segment.y1, segment.y2+increment, increment):
        grid[segment.x1-min_x][j-min_y] = '#'
  return grid

def get_filled_grid(grid):
  result = [['#']*len(grid[0]) for row in grid] 
  to_visit = []
  visited = {}
  for i in range(0, len(grid)):
    if not i == 0 and not i == len(grid) - 1:
      to_visit.append((i, 0))
      to_visit.append((i, len(grid[0]) -1))
      continue
    for j in range(0, len(grid[0])):
      to_visit.append((i, j))
  to_visit = list(filter(lambda x: grid[x[0]][x[1]] == '.', to_visit))
  print(to_visit)
  while to_visit:
    cell = to_visit.pop(0)
    if cell in visited:
      continue
    visited[cell] = True
    result[cell[0]][cell[1]] = '.'
    x, y = cell
    next_cells = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for next_cell in next_cells:
      if next_cell[0] < 0 or next_cell[0] >= len(grid):
        continue
      if next_cell[1] < 0 or next_cell[1] >= len(grid[0]):
        continue
      if (next_cell[0], next_cell[1]) in visited:
        continue
      if grid[next_cell[0]][next_cell[1]] == '#':
        continue
      to_visit.append(next_cell)
  return result

def get_area(grid):
  count = 0
  for row in grid:
    for cell in row:
      if cell == '#':
        count += 1
  print(count)

def main(argv):
  instructions = get_instructions(argv[0])
  min_x, min_y, max_x, max_y, segments = get_segments(instructions)
  print(min_x, min_y, max_x, max_y)
  #[print(str(segment)) for segment in segments]
  grid = build_grid(min_x, min_y, max_x, max_y, segments)
  io.pretty_print(grid)
  filled_grid = get_filled_grid(grid) 
  io.pretty_print(filled_grid)
  get_area(filled_grid)

if __name__ == "__main__":
  main(sys.argv[1:])
