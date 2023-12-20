import sys
import numpy

def pretty_print(array):
  for row in array:
    print(" ".join(list(map(str, row))))

def get_rock_map(input_file):
  rock_map = []
  file = open(input_file, 'r')
  for line in file.readlines():
    row = []
    for x in line.strip():
      row.append(x)
    rock_map.append(row)
  return rock_map

def get_north_map(rock_map):
  north_map = [] 
  blocker = 0
  for col in range(0, len(rock_map[0])):
    column = []
    rock_count = 0
    blank_count = 0
    for row in range(0, len(rock_map)):
      if rock_map[row][col] == '#':
        column.extend(['O']*rock_count)
        column.extend(['.']*blank_count)
        column.append('#')
        rock_count = 0
        blank_count = 0
      elif rock_map[row][col] == 'O':
        rock_count += 1
      else:
        blank_count += 1
    column.extend(['O']*rock_count)
    column.extend(['.']*blank_count)
    north_map.append(column)        
  return numpy.array(north_map).transpose().tolist()

def get_map_value(m):
  sum = 0
  for i, row in enumerate(reversed(m)):
    sum += row.count('O') * (i + 1) 
  return sum

def main(argv):
  rock_map = get_rock_map(argv[0])
  north_map = get_north_map(rock_map)
  print(get_map_value(north_map))

if __name__ == "__main__":
  main(sys.argv[1:])
