import sys
import re
import bisect
from collections import defaultdict

class Brick():
  def __init__(self, name, x1, y1, z1, x2, y2, z2):
    self.name = name
    self.x1 = x1
    self.y1 = y1
    self.z1 = z1
    self.x2 = x2
    self.y2 = y2
    self.z2 = z2
    self.z = 0 
    self.supports = set() 
    self.supported_by = set()

  def __str__(self):
    return '%s: (%s,%s,%s)->(%s,%s,%s) with height %s at z %s supports %s supported by %s' % (self.name, self.x1, self.y1, self.z1, self.x2, self.y2, self.z2, self.height(), self.z, [x.name for x in self.supports], [x.name for x in self.supported_by])

  def height(self):
    return self.z2 - self.z1 + 1

class Grid():
  def __init__(self, max_x, max_y):
    # (x, y) -> [(h, name)]
    self.settled = defaultdict(list) 

  # Find height of bricks in a certain square area
  def add_brick(self, brick):
    max_h, max_bricks = self.find_overlap(brick)  
    self.update(max_h, brick)
    brick.z = max_h
    for max_brick in max_bricks:
      max_brick.supports.add(brick)
      brick.supported_by.add(max_brick)
  
  def update(self, new_h, brick):
    for i in range(brick.x1, brick.x2+1):
      for j in range(brick.y1, brick.y2+1):
        self.settled[(i, j)].append(brick)

  def find_overlap(self, brick):
    max_h = 0
    max_bricks = []
    for i in range(brick.x1, brick.x2+1):
      for j in range(brick.y1, brick.y2+1):
        if (i,j) not in self.settled:
          continue
        settled_brick = self.settled[(i, j)][-1]
        new_height = settled_brick.z + settled_brick.height()
        if new_height == max_h:
          max_bricks.append(settled_brick)
          continue
        if new_height > max_h:
          max_h = new_height 
          max_bricks = [settled_brick]
    if not max_bricks:
      return 0, [] 
    return max_h, max_bricks

  def get_count(self, input):
    counts = defaultdict(int)
    done = set()
    for key, bricks in self.settled.items():
      for brick in bricks:
        if brick in done:
          continue
        done.add(brick)
        for s in brick.supports:
          counts[s.name] += 1
    count = 0
    sum = 0
    for brick in input:
      temp_counts = counts.copy()
      todo = [brick]
      disintegrated = set() 
      while todo:
        current_brick = todo.pop(0)
        for s in current_brick.supports:
          temp_counts[s.name] -= 1 
          if temp_counts[s.name] == 0:
            if s.name not in disintegrated:
              disintegrated.add(s.name)
              todo.append(s) 
      sum += len(disintegrated)
    return sum 
           
def get_bricks(input):
  file = open(input, 'r')
  bricks = []
  max_x = 0
  max_y = 0
  for i, line in enumerate(file.readlines()):
    match = re.match('^(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)$', line.strip())
    brick = Brick(str(i), *tuple(map(int, list(match.group(1, 2, 3, 4, 5, 6)))))
    max_x = max(max_x, brick.x2) 
    max_y = max(max_y, brick.y2)
    bisect.insort(bricks, brick, key=lambda x: x.z1)
  return max_x, max_y, bricks

def main(argv):
  max_x, max_y, bricks = get_bricks(argv[0])
  grid = Grid(max_x, max_y)
  for brick in bricks:
    grid.add_brick(brick)
  done = set()
  for key, settled in grid.settled.items():
    for brick in settled:
      if brick in done:
        continue
      done.add(brick)
  print(grid.get_count(bricks))

if __name__ == "__main__":
  main(sys.argv[1:])
