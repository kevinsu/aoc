def pretty_print(array):
  for row in array:
    print(' '.join(list(map(str, row))))

def get_2d_int_array_from_file(input_file):
  file = open(input_file, 'r')
  return [[int(c) for c in line.strip()] for line in file.readlines()]
