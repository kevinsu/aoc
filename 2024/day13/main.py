import sys
import re
from common.perf import profiler

def solve(ax, ay, bx, by, px, py):
  i = (px * by - py * bx) / (by * ax - ay * bx)
  j = (px * ay - py * ax) / (bx * ay - by * ax)
  if int(i) == i and int(j) == j:    
    return int(i*3 + j)
  return 0

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  matches = re.finditer(r'Button\s.*:\sX\+(\d+),\sY\+(\d+)\sButton\s.*:\sX\+(\d+),\sY\+(\d+)\sPrize:\sX=(\d*),\sY=(\d*)', file.read())
  part1 = 0
  part2 = 0
  for match in matches:
    ax, ay, bx, by, px, py = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)), int(match.group(6))
    part1 += solve(ax, ay, bx, by, px, py)
    part2 += solve(ax, ay, bx, by, px+10000000000000, py+10000000000000)
    
  print(part1)
  print(part2)
    
if __name__ == "__main__":
  main(sys.argv[1:])
