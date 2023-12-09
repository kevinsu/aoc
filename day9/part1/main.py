import sys

def get_line_value(input_line):
  values = list(map(int, input_line.split()))
  list_of_values = [values]
  while not all(value == 0 for value in values):
    diffs = []
    for i in range(0, len(values)-1):
      diffs.append(values[i+1] - values[i]) 
    values = diffs
    list_of_values.append(diffs)
  answer = 0
  return sum([values[-1] for values in list_of_values])
    

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    sum += get_line_value(line)
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
