import sys
from common.perf import profiler
import math

def get_winner(elves):
  remaining = len(elves)
  while remaining > 2:
    target = int(len(elves)/2)
    temp = elves[target]
    elves = elves[1:target]+elves[target+1:]+elves[0:1]
    remaining = len(elves)
  return elves[0]

def get_winner_fast(elves):
  while True:
    if len(elves) < 10:
      return get_winner(elves)
    half = int(len(elves)/2)
    target = math.ceil(len(elves)/3)
    if len(elves)%2 == 0:
      initial = half+2 
    if len(elves)%2 == 1:
      initial = half+1
    elves = elves[target:half] + elves[initial::3] + elves[:target] 
  
  
@profiler
def main(argv):
  n = int(argv[0])
  elves = list(range(1, n+1))
  print(get_winner_fast(elves))

if __name__ == "__main__":
  main(sys.argv[1:])
