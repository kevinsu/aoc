import numpy as np
import re
import sys
from common.perf import profiler

# 1 northwest, 2 northeast, 3 southeast, 4 southwest
def get_quadrant(x, y, height, width):
  middle_x = (height - 1) / 2
  middle_y = (width - 1) / 2
  if x == middle_x or y == middle_y:
    return 0
  if x < middle_x:
    if y < middle_y:
      return 1
    return 2
  if y < middle_y:
    return 4
  return 3

previous_max = 0

def display(points, height, width, steps):
  counts = {}
  for point in points:
    if point[1] not in counts:
      counts[point[1]] = 0
    counts[point[1]] += 1
  max_y = max(counts.values())
  global previous_max
  if max_y >= previous_max:
    previous_max = max_y    
  else:
    return
  print(steps)
  for i in range(0, width):
    line = ''
    for j in range(0, height):
      if (j, i) in points:
        line += '1'
      else:
        line += '.'
    print(line)

def part2(input, height, width):
  steps = 0
  while True:
    points = set()
    for robot in input:
      x = (robot[0] + steps*robot[2]) % height
      y = (robot[1] + steps*robot[3]) % width
      points.add((x, y))    
    display(points, height, width, steps)
    steps += 1
    
def part1(input, height, width, steps):
  quadrant_count = {0: 0, 1: 0, 2: 0, 3: 0, 4:0}
  for robot in input:
    x = (robot[0] + steps*robot[2]) % height
    y = (robot[1] + steps*robot[3]) % width
    if x != height // 2 and y != width // 2:
      print(x, y)    
      quadrant =       (x > height // 2) * 2 + (y > width // 2)
      quadrant = get_quadrant(x, y, height, width)
      quadrant_count[quadrant] += 1    
  del quadrant_count[0]
  return np.prod(np.array(list(quadrant_count.values())))    

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  input = []
  matches = re.finditer(r'p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)', file.read())
  for match in matches:
    input.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
  print(part1(input, 101, 103, 100))
  print(part2(input, 101, 103))
    

if __name__ == "__main__":
  main(sys.argv[1:])
