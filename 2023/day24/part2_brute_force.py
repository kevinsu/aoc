import sys
import re
import itertools
import copy

def get_hailstone(input_line):
  match = re.match('^(\d+),\s(\d+),\s(\d+)\s@\s([\s\-]?\d+),\s([\s\-]?\d+),\s([\s\-]?\d+)$', input_line)
  return list(map(int, match.group(1, 2, 3, 4, 5, 6)))

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

  def clone(self, vx, vy, vz):
    new_h = copy.deepcopy(self)
    new_h.vx = new_h.vx-vx
    new_h.vy = new_h.vy-vy
    new_h.vz = new_h.vz-vz
    return new_h

def close_enough(n1, n2):
  return abs(n2-n1) < 1000

def get_intersection(h1, h2):
  b1 = h1[1] - h1[0]/h1[3]*h1[4]
  m1 = h1[4]/h1[3]
  b2 = h2[1] - h2[0]/h2[3]*h2[4]
  m2 = h2[4]/h2[3]
  if m1 == m2:
    b1 = h1[2] - h1[0]/h1[3]*h1[5]
    m1 = h1[5]/h1[3]
    b2 = h2[2] - h2[0]/h2[3]*h2[5]
    m2 = h2[5]/h2[3]
  if m1 == m2:
    raise Exception("slopes the same")
  x = -(b2 - b1) / (m2 - m1)
  t1 = (x-h1[0])/h1[3]
  t2 = (x-h2[0])/h2[3]
  if not close_enough(h1[2]+h1[5]*t1, h2[2]+h2[5]*t2):
    return None, None, -1
  if t1 >= 0 and t2 >=0:
    return x, m1*x + b1, t1
  return None, None, -1

def get_initial(hailstones, vx, vy, vz):
  new_hailstones = []
  for hailstone in hailstones:
    new_hailstone = copy.copy(hailstone)
    new_hailstone[3] = new_hailstone[3] - vx
    new_hailstone[4] = new_hailstone[4] - vy
    new_hailstone[5] = new_hailstone[5] - vz
    new_hailstones.append(new_hailstone)
  t = 0
  for h1, h2 in itertools.combinations(new_hailstones, 2):
    try:
      x, y, t = get_intersection(h1, h2)
      if t == -1:
        return None, None, None
    except:
      return None, None, None
  return h1[0]+h1[3]*t,h1[1]+h1[4]*t,h1[2]+h1[5]*t    

def brute_force(hailstones, x_ranges, y_ranges, z_ranges):
  i = 0 
  while True: 
    print("Trying combos with i=%s" % i)
    x_range = get_range_from_bad_range(i, x_ranges)
    y_range = get_range_from_bad_range(i, y_ranges)
    z_range = get_range_from_bad_range(i, z_ranges)
    for vx, vy, vz in itertools.product(x_range, y_range, z_range):
      if abs(vx) != i and abs(vy) != i and abs(vz) != i:
        continue
      x, y, z = get_initial(hailstones, vx, vy, vz)
      if x != None:
        return x, y, z
    i+= 1
    if i == 361:
      break

def get_range_from_bad_range(max_value, bad_ranges):
  acceptable = set() 
  for i in range(-max_value, max_value+1):
    acceptable.add(i)
  for bad_range in bad_ranges:
    for i in range(bad_range[0], bad_range[1]+1):
      if i in acceptable:
        acceptable.remove(i)
  return acceptable
    

def get_bad_ranges(hailstones):
  x_ranges = []
  y_ranges = []
  z_ranges = []
  for h1, h2 in itertools.combinations(hailstones, 2):
    if h1[0] > h2[0] and h1[3] > h2[3]:
      x_ranges.append((h2[3], h1[3]))
    elif h1[0] < h2[0] and h1[3] < h2[3]:
      x_ranges.append((h1[3], h2[3]))
    if h1[1] > h2[1] and h1[4] > h2[4]:
      y_ranges.append((h2[4], h1[4]))
    elif h1[1] < h2[1] and h1[4] < h2[4]:
      y_ranges.append((h1[4], h2[4]))
    if h1[2] > h2[2] and h1[5] > h2[5]:
      z_ranges.append((h2[5], h1[5]))
    elif h1[2] < h2[2] and h1[5] < h2[5]:
      z_ranges.append((h1[5], h2[5]))
  return x_ranges, y_ranges, z_ranges

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  hailstones = []
  for line in file.readlines():
    hailstone = get_hailstone(line.strip()) 
    hailstones.append(hailstone)
  bad_ranges = get_bad_ranges(hailstones)
  x, y, z = brute_force(hailstones, *bad_ranges)
  #x, y, z = get_initial(hailstones, 47, -360, 18)
  print(x + y + z)

if __name__ == "__main__":
  main(sys.argv[1:])
