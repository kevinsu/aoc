import sys
from common.perf import profiler

def update_pos(c, x, y):
  if c == 'U':
    y -= 1
  elif c == 'D':
    y += 1
  elif c == 'L':
    x -= 1
  else:
    x += 1 
  return x, y

def part1(line, x, y):
  for c in line.strip():
    x, y = update_pos(c, x, y)
    if x > 3:
      x = 3
    elif x < 1:
      x = 1
    if y > 2:
      y = 2
    if y < 0:
      y = 0
  return y*3 + x, x, y 

KEYPAD = {
  (0, 0) : '7',
  (0, 1) : 'B',
  (1, 0) : '8',
  (0, -1) : '3',
  (-1, 0) : '6',
  (0, 2) : 'D',
  (-1, 1) : 'A',
  (-2, 0) : '5',
  (-1, -1) : '2',
  (0, -2) : '1',
  (1, -1) : '4',
  (2, 0) : '9',
  (1, 1) : 'C',
}
def part2(line, x, y):
  for c in line.strip():
    prev = (x, y)
    x, y = update_pos(c, x, y)
    if abs(x) + abs(y) > 2:
      x, y = prev
  return KEYPAD[(x, y)], x, y
    

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  x1 = 2
  y1 = 1
  x2 = -2 
  y2 = 0
  code1 = ''
  code2 = ''
  for line in file.readlines():
    c1, x1, y1 = part1(line.strip(), x1, y1)
    code1 += str(c1)
    c2, x2, y2 = part2(line.strip(), x2, y2)
    code2 += str(c2)
  print('part1: ', code1)
  print('part2: ', code2)
    

if __name__ == "__main__":
  main(sys.argv[1:])
