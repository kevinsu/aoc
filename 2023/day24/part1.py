import sys
import re
import itertools

class Hailstone:
  def __init__(self, input_line):
    match = re.match('^(\d+),\s(\d+),\s(\d+)\s@\s([\s\-]?\d+),\s([\s\-]?\d+),\s([\s\-]?\d+)$', input_line)    
    self.x = int(match.group(1))
    self.y = int(match.group(2))
    self.z = int(match.group(3))
    self.vx = int(match.group(4))
    self.vy = int(match.group(5))
    self.vz = int(match.group(6))

  def __str__(self):
    return ('%s,%s,%s @ %s,%s,%s' % (self.x, self.y, self.z, self.vx, self.vy, self.vz))

  def get_intersection(self, other):
    b1 = self.y - self.x/self.vx*self.vy
    m1 = self.vy/self.vx
    b2 = other.y - other.x/other.vx*other.vy
    m2 = other.vy/other.vx
    if m1 == m2:
      return None, None
    x = -(b2 - b1) / (m2 - m1)
    t1 = (x-self.x)/self.vx
    t2 = (x-other.x)/other.vx
    if t1 >= 0 and t2 >=0:
      return x, m1*x + b1
    return None, None

def count_intersections(hailstones, min_val, max_val):
  count = 0
  for h1, h2 in itertools.combinations(hailstones, 2):
    x, y = h1.get_intersection(h2)
    if x == None:
      continue 
    if x >= min_val and x <= max_val and y >= min_val and y <= max_val:
      count+=1
  return count

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  hailstones = []
  for line in file.readlines():
    hailstone = Hailstone(line.strip())
    hailstones.append(hailstone)
  print(count_intersections(hailstones, 200000000000000, 400000000000000))

if __name__ == "__main__":
  main(sys.argv[1:])
