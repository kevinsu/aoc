import re
import sys
from common.perf import profiler

def get_lock_heights(lock):
  heights = []
  for j in range(len(lock[0])):
    height = -1
    for i in range(len(lock)):
      if lock[i][j] == '#':
        height += 1
        continue
    heights.append(height)    
  return heights

def get_key_heights(key):
  heights = []
  for j in range(len(key[0])):
    height = -1
    for i in range(len(key)-1, -1, -1):
      if key[i][j] == '#':
        height += 1
        continue
    heights.append(height)
  return heights

def count(keys, locks):
  sum = 0
  for key in keys:
    for lock in locks:
      overlap = False
      for i in range(len(key)):
        if key[i] + lock[i] >= 6:
          overlap = True
          break
      if not overlap:
        print(key, lock)
        sum += 1
  return sum

        
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  current = []
  keys = []
  locks = []
  for line in file.readlines():
    if line == '\n':
      if current[0] == '.....':
        keys.append(get_key_heights(current))
      else:
        locks.append(get_lock_heights(current))
      current = []
    else:
      current.append(line.strip())
  if current[0] == '.....':
    keys.append(get_key_heights(current))
  else:
    locks.append(get_lock_heights(current))  
  print(count(keys, locks))
  
if __name__ == "__main__":
  main(sys.argv[1:])
