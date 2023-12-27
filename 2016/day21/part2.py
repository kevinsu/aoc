import sys
from common.perf import profiler
from part1 import *

def swap(input, line):
  splits = line.split()
  index1 = None
  index2 = None
  if splits[1] == 'position':
    index1 = int(splits[2])
    index2 = int(splits[5])
  else:
    index1 = input.index(splits[2])
    index2 = input.index(splits[5]) 
  if index2 < index1:
    temp = index1
    index1 = index2
    index2 = temp
  return input[0:index1]+input[index2]+input[index1+1:index2]+input[index1]+input[index2+1:]

def reverse(input, line):
  splits = line.split()
  index1 = int(splits[2])
  index2 = int(splits[4])
  return input[0:index1]+input[index1:index2+1][::-1]+input[index2+1:]

def rmove(input, line):
  splits = line.split()
  new_line = 'move position %s to position %s' % (splits[5], splits[2])
  return move(input, new_line)

def rrotate(input, line, reverse_map):
  splits = line.split()
  if splits[1] == 'left':
    new_line = 'rotate right %s steps' % splits[2]
    return rotate(input, new_line)
  if splits[1] == 'right':
    new_line = 'rotate left %s steps' % splits[2]
    return rotate(input, new_line)
  else:
    index = input.index(splits[6])
    new_line = 'rotate left %s steps' % reverse_map[index] 
    return rotate(input, new_line)

def build_reverse_map(input):
  reverse_map = {}
  for i, c in enumerate(input):
    rotated = rotate(input, f"rotate based on position of letter {c}")
    reverse_map[rotated.index(c)] = rotated.index(input[0])
  return reverse_map 

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  input = argv[1] 
  reverse_map = build_reverse_map(input)
  for line in reversed(file.readlines()):
    if line.startswith('swap'):
      input = swap(input, line)
    elif line.startswith('reverse'):
      input = reverse(input, line)
    elif line.startswith('rotate'):
      input = rrotate(input, line, reverse_map)
    elif line.startswith('move'):
      input = rmove(input, line)
  print(input)

if __name__ == "__main__":
  main(sys.argv[1:])
