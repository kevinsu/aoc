import sys
from common.perf import profiler
from common.grid import display

def rect(grid, x, y):
  for i in range(0, x):
    for j in range(0, y):
      grid[j][i] = '#' 

def rotate_row(grid, row, steps):
  grid[row] = grid[row][-steps:] + grid[row][:-steps]

def rotate_col(grid, col, steps):
  column = [row[col] for row in grid]
  for i in range(0, len(grid)):
    grid[(i+steps)%len(grid)][col] = column[i]

@profiler
def main(argv):
  input_file = argv[0]
  x, y = int(argv[1]), int(argv[2])
  grid = [['.']*y for i in range(0, x)]
  file = open(input_file, 'r')
  for line in file.readlines():
    splits = line.split()
    if splits[0] == 'rect':
      x, y = splits[1].split('x')
      rect(grid, int(x), int(y)) 
    elif splits[0] == 'rotate':
      if splits[1] == 'row':
        rotate_row(grid, int(splits[2].split('=')[1]), int(splits[4]))
      else:
        rotate_col(grid, int(splits[2].split('=')[1]), int(splits[4]))
  print('part 1: ', sum(row.count('#') for row in grid))
  print('part 2:')
  display(grid)

if __name__ == "__main__":
  main(sys.argv[1:])
