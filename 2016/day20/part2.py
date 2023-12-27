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
  intervals.append((4294967295, 4294967296))
  eligible = []
  next_eligible = 0
  start_blacklist = None
  for interval in sorted(intervals):
    if next_eligible < interval[0]:
      eligible.append((next_eligible, interval[0]-1))
    next_eligible = max(interval[1]+1, next_eligible) 
  sum = 0
  for x, y in eligible:
    sum+= y-x+1
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
