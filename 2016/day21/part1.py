import sys
from common.perf import profiler

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

def move(input, line):
  splits = line.split()
  index1 = int(splits[2])
  index2 = int(splits[5])
  if index1 < index2:
    return input[0:index1]+input[index1+1:index2+1]+input[index1]+input[index2+1:]
  else:
    return input[0:index2]+input[index1]+input[index2:index1]+input[index1+1:]

def rotate(input, line):
  splits = line.split()
  if splits[1] == 'left':
    index = int(splits[2])
    return input[index:]+input[0:index]
  elif splits[1] == 'right':
    index = int(splits[2])
    return input[-index:]+input[:-index]
  else:
    index = input.index(splits[6]) 
    if index >= 4:
      index += 1
    index+=1
    index = index % len(input)
    return input[-index:]+input[:-index]

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  input = argv[1] 
  for line in file.readlines():
    if line.startswith('swap'):
      input = swap(input, line)
    elif line.startswith('reverse'):
      input = reverse(input, line)
    elif line.startswith('rotate'):
      input = rotate(input, line)
    elif line.startswith('move'):
      input = move(input, line)
  print(input)

if __name__ == "__main__":
  main(sys.argv[1:])
