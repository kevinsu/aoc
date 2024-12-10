import sys
from common.perf import profiler

def compact(line):
  raw = list(line)
  front_index = 0 
  back_index = len(raw)-1
  while front_index < back_index:
    front = raw[front_index]
    back = raw[back_index]
    if front != '.':
      front_index += 1
      continue
    raw[front_index] = back
    raw[back_index] = '.'
    back_index -= 1
  return raw

def get_checksum(line):
  sum = 0
  for i, c in enumerate(line):
    if c == '.':
      continue
    sum += i * int(c)
  return sum

def part1(line):
  uncompacted = []
  file_id = 0
  space = False
  for char in line:
    if space:
      uncompacted.extend(int(char)*['.'])
    else:
      uncompacted.extend([str(file_id)]*int(char))
      file_id += 1
    space = not space
  compacted = compact(uncompacted)
  return get_checksum(compacted)

def get_front_index(raw, num):
  front_index = len(raw)
  for i in range(0, len(raw)-num):
      open = True
      if raw[i] != '.':
        continue
      for j in range(1, num):
        if raw[i+j] != '.':
          open = False
          break
      if open:        
        front_index = i 
        break
  return front_index         

def compact2(line):
  raw = list(line)
  back_index = len(raw)-1
  while back_index > 0:
    back = raw[back_index]
    if back == '.':
      back_index -= 1
      continue
    back_start_index = back_index
    while raw[back_index] == raw[back_start_index]:
      back_start_index -= 1
    num = back_index - back_start_index
    front_index = get_front_index(raw, num)
    if front_index >= back_index:
      back_index = back_start_index
      continue
    
    front_end_index = front_index
    while raw[front_index] == raw[front_end_index]:
      front_end_index += 1
    # Doesn't fit
    if back_index - back_start_index > front_end_index - front_index:
      back_index = back_start_index
      continue
    for i in range(0, back_index - back_start_index):
      raw[front_index+i] = back
      raw[back_index-i] = '.'
    back_index = back_start_index
  return raw

def part2(line):
  uncompacted = []
  file_id = 0
  space = False
  for char in line:
    if space:
      uncompacted.extend(int(char)*['.'])
    else:
      uncompacted.extend([str(file_id)]*int(char))
      file_id += 1
    space = not space
  compacted = compact2(uncompacted)
  return get_checksum(compacted)
      
  
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  line = file.readline()
  print(part1(line))
  print(part2(line))
  
if __name__ == "__main__":
  main(sys.argv[1:])
