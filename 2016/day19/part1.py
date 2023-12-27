import sys
from common.perf import profiler

def get_winner(elves):
  remaining = len(elves)
  while remaining > 2:
    if remaining %2 == 0:
      elves = elves[::2] 
    else:
      elves = elves[2::2]
    remaining = len(elves)
  return elves[0]

@profiler
def main(argv):
  n = int(argv[0])
  elves = list(range(1, n+1))
  print(get_winner(elves))

if __name__ == "__main__":
  main(sys.argv[1:])
