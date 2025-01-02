import sys
from itertools import combinations
from common.perf import profiler

def part1(connections):
  connected = set()
  for one, value in connections.items():
    for two, three in combinations(value, 2):
      if three in connections[two]:
        if one.startswith('t') or two.startswith('t') or three.startswith('t'):        
          connected.add(get_set_name([one, two, three]))
  return len(connected)

def get_set_name(candidates):
  return ",".join(sorted(candidates))

def part2(connections):
  connected = set()
  for one, value in connections.items():
    for two, three in combinations(value, 2):
      if three in connections[two]:
        connected.add(get_set_name([one, two, three]))
  for i in range(3, 100):
    added = False
    for host, value in connections.items():
      if len(value) < i:
        continue
      for candidates in combinations(value, i):
        set_name = get_set_name(candidates)
        if set_name in connected:
          added = True
          connected.add(get_set_name(list(candidates)+[host]))
    if not added:
      break
  return max(connected, key=len)

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  connections = {}
  for line in file.readlines():
    left, right = line.strip().split('-')
    if left not in connections:
      connections[left] = set()
    connections[left].add(right)
    if right not in connections:
      connections[right] = set()
    connections[right].add(left)
  #print(part1(connections))
  print(part2(connections))

if __name__ == "__main__":
  main(sys.argv[1:])
