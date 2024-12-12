import sys
from common.perf import profiler

seen = {}

def count_stones(stone, blinks):  
  if (stone, blinks) in seen:
    return seen[(stone, blinks)] 
  if blinks == 0:
    return 1
  if blinks == 1:
    return 1 if stone == 0 or stone == 1 or len(str(stone))%2 == 1 else 2
  if stone == 0:
    result = count_stones(1, blinks-1)
    
  elif len(str(stone)) % 2 == 0:
    left = int(str(stone)[0:int(len(str(stone))/2)])
    
    right = int(str(stone)[int(len(str(stone))/2):])
    result = count_stones(left, blinks-1) + count_stones(right, blinks-1)
    
  else:
    result = count_stones(stone*2024, blinks-1)
  seen[(stone, blinks)] = result
  return result
      

def solve(line, blinks):
  stones = line.split()
  sum = 0
  for stone in stones:
    sum += count_stones(int(stone), blinks)
  return sum

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  line = file.readline()
  print(solve(line, 25))
  print(solve(line, 75))

if __name__ == "__main__":
  main(sys.argv[1:])
