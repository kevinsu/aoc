import itertools
import re
import sys
from common.perf import profiler
from common.twod import get_intersection

def part1(sensors, row):
  # For each sensor, find points on a row that cannot contain a beacon
  # Get the row difference, then add remainder to the column +/-
  restricted = set()
  beacons = set()
  for sensor in sensors:
    sx, sy, bx, by = sensor
    beacons.add((bx, by))
    manhattan = abs(bx-sx) + abs(by-sy)
    remaining = manhattan - abs(sy - row)
    for i in range(-remaining, remaining+1):
      restricted.add((sx+i, row))
  return len(restricted.difference(beacons))

def get_manhattan(x, y, distance):
  for i in range(distance+1):
    yield x + i, y + distance + 1 - i
    yield x + distance +1 - i, y - i
    yield x - i, y - distance -1 + i
    yield x - distance -1 + i, y + i

def get_possibilities(x, y, distance):
  for i in range(3):
    yield x + i, y + distance + 1 - i
    yield x + distance +1 - i, y - i
    yield x - i, y - distance -1 + i
    yield x - distance -1 + i, y + i

def get_line_segments(x, y, distance):
  yield (x+distance, y, x, y-distance)
  yield (x, y-distance, x-distance, y)
  yield (x-distance, y, x, y+distance)
  yield (x, y+distance, x+distance, y)

def part2(sensors, beacons, limit):
  possibilities = set()
  line_segments = set()
  for sensor in sensors:
    sx, sy, bx, by = sensor
    manhattan = abs(bx-sx) + abs(by-sy)
    for x1, y1, x2, y2 in get_line_segments(sx, sy, manhattan+1):
      line_segments.add((x1, y1, x2, y2))
  for ls1, ls2 in itertools.combinations(line_segments, 2):
    intersection = get_intersection(ls1, ls2)
    if not intersection:
      continue
    x, y = intersection
    if x < 0 or x > limit or y < 0 or y > limit:
      continue
    possibilities.add((int(x), int(y)))  
  for p in possibilities:
    eligible = True
    px, py = p
    for sensor in sensors:
      sx, sy, bx, by = sensor
      manhattan = abs(bx-sx) + abs(by-sy)
      test_manhattan = abs(px-sx) + abs(py-sy)
      if test_manhattan <= manhattan:
        eligible = False
        break
    if eligible:
      return px, py
  return 0

def brute_force(sensors, beacons, limit):
  borders = set()
  possibilities = set()
  for sensor in sensors:
    print(sensor)
    sx, sy, bx, by = sensor
    manhattan = abs(bx-sx) + abs(by-sy)
    for x, y in get_possibilities(sx, sy, manhattan):
      print(x, y)
      if x < 0 or x > limit:
        continue
      if y < 0 or y > limit:
        continue
      if (x, y) in borders and (x, y) not in beacons:
        possibilities.add((x, y))        
      borders.add((x, y))
  count = 0
  for p in possibilities:
    count += 1
    eligible = True
    px, py = p
    for sensor in sensors:
      sx, sy, bx, by = sensor
      manhattan = abs(bx-sx) + abs(by-sy)
      test_manhattan = abs(px-sx) + abs(py-sy)
      if test_manhattan <= manhattan:
        eligible = False
        break
    if eligible:
      return px, py
  return 0

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sensors = set()
  beacons = set()
  for line in file.readlines():
    match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    sx, sy, bx, by = match.groups()
    sensors.add((int(sx), int(sy), int(bx), int(by)))
    beacons.add((int(bx), int(by)))    
  print(part1(sensors, 2000000))  
  print(part2(sensors, beacons, 4000000))  
if __name__ == "__main__":
  main(sys.argv[1:])
