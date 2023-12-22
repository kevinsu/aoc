def pretty_print(array):
  for row in array:
    print(' '.join(list(map(str, row))))
  print()

def get_2d_int_input(input_file):
  file = open(input_file, 'r')
  return [[int(c) for c in line.strip()] for line in file.readlines()]

def get_2d_string_input(input_file):
  file = open(input_file, 'r')
  return [[c for c in line.strip()] for line in file.readlines()]
