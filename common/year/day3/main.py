import re
import sys
from common.perf import profiler

def part1(input):
  matches = re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', input)
  part1 = 0
  part2 = 0 
  do = True
  for match in matches:
    print(match.group(0))
    if match.group(0).startswith('don\'t'):
      do = False      
    elif match.group(0).startswith('do'):
      do = True     
    else:
      if do:
        part2 += int(match.group(1)) * int(match.group(2))
      part1 += int(match.group(1)) * int(match.group(2))    
  print(part1)
  print(part2)

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  input = file.read()
  part1(input)
  
if __name__ == "__main__":
  main(sys.argv[1:])
