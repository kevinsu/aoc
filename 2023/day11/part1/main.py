import sys

def expand_universe(pre_expand, row_map, column_map):
  universe = []
  row_offset = 0
  galaxies = []
  for i, row in enumerate(pre_expand):
    expanded_row = []
    column_offset = 0
    for j, galaxy in enumerate(row):
      if galaxy == '#':
        galaxies.append((i+row_offset, j+column_offset))
      expanded_row.append(pre_expand[i][j])
      if j not in column_map:
        column_offset += 1
        expanded_row.append(pre_expand[i][j]) 
    universe.append(expanded_row)
    if i not in row_map:
      universe.append(expanded_row)
      row_offset += 1
  return universe, galaxies
       

def build_universe(input_file):
  universe = [] 
  pre_expand = [] 
  row_map = {}
  column_map = {}
  file = open(input_file, 'r')
  for i, line in enumerate(file.readlines()):
    row = []
    for j, galaxy in enumerate(line.strip()):
      if galaxy == '#':
        if i not in row_map:
          row_map[i] = True
        if j not in column_map:
          column_map[j] = True  
      row.append(galaxy)
    pre_expand.append(row)
  universe, galaxies = expand_universe(pre_expand, row_map, column_map)
  return universe, galaxies

def calculate_distances(galaxies):
  sum = 0
  for i in range(0, len(galaxies)):
    for j in range(i, len(galaxies)):
      sum += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
  return sum 

def pretty_print(universe):
  for row in universe:
    line = []
    for galaxy in row:
      line.append(galaxy) 
    print(' '.join(line))

def main(argv):
  input_file = argv[0]
  universe, galaxies = build_universe(input_file)
  print(calculate_distances(galaxies))

if __name__ == "__main__":
  main(sys.argv[1:])
