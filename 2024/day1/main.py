import sys
from common.perf import profiler

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  result = 0
  left = []
  right = []
  left_map = {}
  right_map = {}
  for line in file.readlines():    
    l, r = line.split()
    l = int(l)
    r = int(r)
    if l not in left_map:
      left_map[l] = 0
    if r not in right_map:
      right_map[r] = 0
    left_map[l] += 1
    right_map[r] += 1
    left.append(l)
    right.append(r)
  left.sort()
  right.sort()  
  for l, r in zip(left, right):
    result += abs(r-l)
  similarity = 0
  for i in left:
    similarity += i * right_map.get(i, 0)  
  print(result)
  print(similarity)

if __name__ == "__main__":
  main(sys.argv[1:])
