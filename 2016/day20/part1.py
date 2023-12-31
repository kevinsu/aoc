import sys
from common.perf import profiler

@profiler
def main(argv):
  input_file = argv[0]
  intervals = []
  file = open(input_file, 'r')
  for line in file.readlines():
    splits = line.strip().split('-')
    intervals.append((int(splits[0]), int(splits[1])))
  next_eligible = 0
  for interval in sorted(intervals):
    if interval[0] > next_eligible:
      break
    next_eligible = max(next_eligible, interval[1]+1)
  print(next_eligible)

if __name__ == "__main__":
  main(sys.argv[1:])
