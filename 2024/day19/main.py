import sys
from common.perf import profiler

def possible(designs, pattern):
  candidates = [pattern]
  seen = set()
  while candidates:
    candidate = candidates.pop()
    if candidate in seen:
      continue
    seen.add(candidate)
    for design in designs:
      if len(candidate) == 0:
        return True
      if not candidate.startswith(design):
        continue
      candidates.append(candidate[len(design):])      
  return False

def count(designs, pattern, seen):
  sum = 0
  if len(pattern) == 0:
    return 1
  if pattern in seen:
    return seen[pattern]
  for design in designs:
    if not pattern.startswith(design):
      continue
    sum += count(designs, pattern[len(design):], seen)
  seen[pattern] = sum
  return sum  


def part1(designs, patterns):
  sum = 0
  for pattern in patterns:
    if possible(designs, pattern):      
      sum += 1
  return sum

def part2(designs, patterns):
  sum = 0
  for pattern in patterns:
    res = count(designs, pattern, {})
    sum += res
  return sum

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  designs = file.readline().strip().split(", ")
  file.readline()
  patterns = []
  for line in file.readlines():
    patterns.append(line.strip())
  print(part1(designs, patterns))    
  print(part2(designs, patterns))    

if __name__ == "__main__":
  main(sys.argv[1:])
