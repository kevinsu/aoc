import sys

def hash(step):
  current_value = 0
  for c in step:
    current_value += ord(c)
    current_value *= 17
    current_value %= 256
  return current_value
    

def parse_line(line):
  steps = line.strip().split(",")
  sum = 0
  for step in steps:
    sum += hash(step)
  print(sum)
    


def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  parse_line(file.readline())

if __name__ == "__main__":
  main(sys.argv[1:])
