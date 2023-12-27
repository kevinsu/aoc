import sys
from common.perf import profiler

DIRS = {
  'R': {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
  },
  'L': {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N',
  }
}

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  x = 0
  y = 0
  heading = 'N'
  visited = set({0, 0})
  part2 = None
  for instruction in file.readline().strip().split(', '):
    dir = instruction[0]
    length = int(instruction[1:])
    heading = DIRS[dir][heading] 
    for i in range(0, length):
      if heading == 'N':
        y+= 1
      elif heading == 'S':
        y-= 1
      elif heading == 'E':
        x+= 1
      elif heading == 'W':
        x-= 1
      if (x, y) in visited and not part2:
        part2 = (x, y)
      visited.add((x, y))
  print(abs(x) + abs(y))
  print(abs(part2[0]) + abs(part2[1]))

if __name__ == "__main__":
  main(sys.argv[1:])
