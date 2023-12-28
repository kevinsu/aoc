import sys
from collections import defaultdict
from common.perf import profiler

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  line = file.readline()
  trackers = []
  for c in line.strip():
    d = defaultdict(int)
    d[c] = 1
    trackers.append(d)
  for line in file.readlines():
    for i, c in enumerate(line.strip()):
      trackers[i][c] += 1
  print('part 1: ', ''.join([max(d, key=d.get) for d in trackers]))
  print('part 2: ', ''.join([min(d, key=d.get) for d in trackers]))

if __name__ == "__main__":
  main(sys.argv[1:])
