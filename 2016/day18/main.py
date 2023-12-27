import sys
from common.perf import profiler

IS_TRAP = {'..^', '^..', '^^.', '.^^'}

def get_next_line(line):
  border = '.' + line[:2]
  result = '^' if border in IS_TRAP else '.' 
  for i in range(1, len(line)-1):
    result += '^' if line[i-1:i+2] in IS_TRAP else '.'
  border = line[-2:] + '.'
  result += '^' if border in IS_TRAP else '.' 
  return result

@profiler
def main(argv):
  input_file = argv[0]
  num_rows = int(argv[1])
  file = open(input_file, 'r')
  line = file.readline().strip()
  print(line)
  i = 1
  sum = line.count('.')
  seen = {}
  jumped = False
  while i < num_rows:
    if not jumped and line in seen:
      cycle_length = i - seen[line][0]
      cycle_sum = sum - seen[line][1]
      num_cycles = int((num_rows - i)/cycle_length)
      i += cycle_length * num_cycles
      sum += cycle_sum * num_cycles
      jumped = True 
      continue
    seen[line] = (i, sum)
    i+=1
    line = get_next_line(line) 
    sum += line.count('.')
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
