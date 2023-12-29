import sys
from common.perf import profiler

def get_decompressed_length(input):
  i = 0
  length = 0
  open = False
  saved = ''
  while i < len(input):
    c = input[i]
    if c == '(':
      open = True
      i+=1
      continue 
    elif c == ')':
      open = False
      num_chars, repeat = saved.split('x')
      length += int(num_chars) * int(repeat) 
      i+=1 + int(num_chars)
      saved = ''
      continue
    if open:
      saved+=input[i]
    else:
      length+=1
    i+=1
  return length

def part2(input):
  i = 0
  length = 0
  open = False
  saved = ''
  while i < len(input):
    c = input[i]
    if c == '(':
      open = True
      i+=1
      continue
    elif c == ')':
      open = False
      num_chars, repeat = map(int, saved.split('x'))
      length += repeat * part2(input[i+1:i+1+num_chars])
      i+=1 + num_chars
      saved = ''
      continue
    if open:
      saved+=input[i]
    else:
      length+=1
    i+=1
  return length  
      
    

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  for line in file.readlines():
    print('part 1: ', get_decompressed_length(line.strip()))
    print('part 2: ', part2(line.strip()))

if __name__ == "__main__":
  main(sys.argv[1:])
