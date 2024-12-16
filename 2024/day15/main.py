import sys
from common.perf import profiler
from common.io import pretty_print

DIRECTIONS = {
  '<' : (0, -1),
  '>' : (0, 1),
  'v' : (1, 0),
  '^' : (-1, 0),
}

def gps_sum(grid):
  sum = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == '[':
        sum += i*100+j
  return sum

def part1(grid, instructions):
  robot = (0, 0)
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == '@':
        robot = (i, j)

  for instruction in instructions:
    direction = DIRECTIONS[instruction]
    candidate = (robot[0] + direction[0], robot[1] + direction[1])
    if grid[candidate[0]][candidate[1]] == '#':
      continue
    elif grid[candidate[0]][candidate[1]] == '.':
      grid[robot[0]][robot[1]] = '.'
      grid[candidate[0]][candidate[1]] = '@'
      robot = candidate
      continue      
    next_square = candidate
    while grid[next_square[0]][next_square[1]] == 'O':      
      next_square = (next_square[0] + direction[0], next_square[1] + direction[1])
    if grid[next_square[0]][next_square[1]] == '#':
      continue
    grid[robot[0]][robot[1]] = '.'
    grid[candidate[0]][candidate[1]] = '@'
    robot = candidate
    grid[next_square[0]][next_square[1]] = 'O'       
  return gps_sum(grid)

def is_box(grid, x, y):
  return grid[x][y] == '[' or grid[x][y] == ']'

def shift_boxes_horizontal(grid, boxes, dx, dy):
  for box in reversed(boxes[:-1]):
    bx = box[0] + dx
    by = box[1] + dy
    grid[bx][by] = grid[box[0]][box[1]]

def shift_boxes_vertical(grid, rows_of_boxes, dx, dy):
  for row_of_boxes in reversed(rows_of_boxes[:-1]):
    for box in row_of_boxes:
      bx = box[0] + dx
      by = box[1] + dy
      grid[bx][by] = grid[box[0]][box[1]]  
      grid[box[0]][box[1]] = '.'
  
def rep_invariant(grid):
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] != ']' or grid[i][j] != '[':
        continue
      if grid[i][j] == ']':
        assert grid[i][j-1] == '['
      if grid[i][j] == '[':
        assert grid[i][j+1] == ']'

def part2(grid, instructions):
  rx = 0
  ry = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == '@':
        rx = i
        ry = j
        break
  
  for instruction in instructions:
    rep_invariant(grid)
    dx, dy = DIRECTIONS[instruction]
    cx = rx + dx
    cy = ry + dy
    if grid[cx][cy] == '#':
      continue
    elif grid[cx][cy] == '.':
      grid[rx][ry] = '.'
      grid[cx][cy] = '@'
      rx = cx
      ry = cy      
      continue      
    if instruction == '<' or instruction == '>':
      # Horizontal
      boxes = []    
      boxes.append((cx, cy))
      nx = cx
      ny = cy
      while is_box(grid, nx, ny):
        nx = nx + dx
        ny = ny + dy
        boxes.append((nx, ny))
      if grid[nx][ny] == '#':
        continue
      shift_boxes_horizontal(grid, boxes, dx, dy)
      grid[cx][cy] = '@'
      grid[rx][ry] = '.'      
    else:
      # Vertical
      rows_of_boxes = []      
      row_of_boxes = set()
      row_of_boxes.add((cx, cy))        
      if grid[cx][cy] == '[':
        row_of_boxes.add((cx, cy+1))        
      elif grid[cx][cy] == ']':
        row_of_boxes.add((cx, cy-1))
      rows_of_boxes.append(row_of_boxes)  
      blocked = False        
      while len(row_of_boxes) > 0:
        next_row_of_boxes = set()
        for box in row_of_boxes:
          nx = box[0] + dx
          ny = box[1] + dy
          if grid[nx][ny] == '#':
            row_of_boxes = set()
            rows_of_boxes = []
            blocked = True
            break
          if grid[nx][ny] == '.':
            continue
          next_row_of_boxes.add((nx, ny))        
          if grid[nx][ny] == '[':
            next_row_of_boxes.add((nx, ny+1))        
          elif grid[nx][ny] == ']':
            next_row_of_boxes.add((nx, ny-1))          
        if not blocked:
          rows_of_boxes.append(next_row_of_boxes)
        row_of_boxes = next_row_of_boxes
      if len(rows_of_boxes) == 0:
        continue
      shift_boxes_vertical(grid, rows_of_boxes, dx, dy)
      grid[cx][cy] = '@'
      grid[rx][ry] = '.'      
    rx = cx
    ry = cy  
  return gps_sum(grid)

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  get_instructions = False
  instructions = None
  grid = []
  wide_grid = []
  for line in file.readlines():
    if line == '\n':
      get_instructions = True
      continue
    if get_instructions:
      instructions = line.strip()
      continue
    grid.append([c for c in line.strip()])
    wide_line = []
    for c in line.strip():
      if c == '#':
        wide_line.extend(['#', '#'])
      elif c == 'O':
        wide_line.extend(['[', ']'])
      elif c == '@':
        wide_line.extend(['@', '.'])
      else:
        wide_line.extend(['.', '.'])
    wide_grid.append(wide_line)
  #print(part1(grid, instructions))
  print(part2(wide_grid, instructions))  

if __name__ == "__main__":
  main(sys.argv[1:])
