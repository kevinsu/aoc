import sys

def round20(n):
  return int(round(n/20)*20)

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  cycle = 1
  x = 1
  check = True
  sum = 0
  values = []
  for line in file.readlines():
    split = line.split()
    if split[0] == 'addx':
      values.extend([x]*2)
      cycle += 2 
      x += int(split[1])
    else:
      values.append(x) 
      cycle += 1
    if check and cycle % 40 in (19, 20):
      sum += round20(cycle)*x
      check = False
    if cycle % 40 in (0, 1 ):
      check = True
  result = ''
  for i in range(0, len(values)):
    if i % 40 == 0:
      result += '\n'
    value = values[i]
    if i % 40 >= value - 1 and i % 40 <= value + 1:
      result += '#'
    else:
      result += '.'
  print(sum)
  print(result)
 

if __name__ == "__main__":
  main(sys.argv[1:])
