import sys
import itertools
import re
from common.perf import profiler

def build_grid(input):
  file = open(input, 'r')
  grid = {}
  for line in file.readlines()[2:]:
    match = re.match('^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+).*', line)
    grid[(int(match.group(1)), int(match.group(2)))] = tuple(map(int, match.group(3, 4, 5, 6)))
  return grid
    
@profiler
def main(argv):
  grid = build_grid(argv[0])
  count = 0
  for f1, f2 in itertools.combinations(grid.values(), 2):
    if f1[1] != 0 and f1[1] <= f2[2]:
      count += 1 
    if f2[1] != 0 and f2[1] <= f1[2]:
      count += 1
  print(count)

if __name__ == "__main__":
  main(sys.argv[1:])
