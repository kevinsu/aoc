import sys

EXPANSION_RATE = 1000000 

def build_universe(input_file):
  universe = [] 
  galaxies = []
  row_map = {}
  column_map = {}
  file = open(input_file, 'r')
  for i, line in enumerate(file.readlines()):
    row = []
    for j, galaxy in enumerate(line.strip()):
      if galaxy == '#':
        galaxies.append((i, j))
        if i not in row_map:
          row_map[i] = True
        if j not in column_map:
          column_map[j] = True  
      row.append(galaxy)
    universe.append(row)
  row_expand_count = 0
  row_expansions = []
  for i in range(0, len(universe)):
    if i not in row_map:
      row_expand_count += 1
    row_expansions.append(row_expand_count)
  column_expand_count = 0
  column_expansions = []
  for i in range(0, len(universe[0])):
    if i not in column_map:
      column_expand_count += 1
    column_expansions.append(column_expand_count)
  print(calculate_distances(galaxies, row_expansions, column_expansions)) 

def calculate_distances(galaxies, row_expansions, column_expansions):
  sum = 0
  for i in range(0, len(galaxies)):
    for j in range(i+1, len(galaxies)):
      galaxy1 = galaxies[i]
      galaxy2 = galaxies[j]
      row_expansion_count = abs(row_expansions[galaxy1[0]] - row_expansions[galaxy2[0]])
      column_expansion_count = abs(column_expansions[galaxy1[1]] - column_expansions[galaxy2[1]])
      row_diff = abs(galaxy1[0] - galaxy2[0])
      column_diff = abs(galaxy1[1] - galaxy2[1])
      row_sum = row_diff - row_expansion_count + row_expansion_count * EXPANSION_RATE 
      column_sum = column_diff - column_expansion_count + column_expansion_count * EXPANSION_RATE
      sum += row_sum + column_sum
      print(i, j, galaxy1, galaxy2, row_expansion_count, column_expansion_count, row_diff, column_diff, row_sum, column_sum)
  return sum 

def pretty_print(universe):
  for row in universe:
    line = []
    for galaxy in row:
      line.append(galaxy) 
    print(' '.join(str(x) for x in line))

def main(argv):
  input_file = argv[0]
  build_universe(input_file)

if __name__ == "__main__":
  main(sys.argv[1:])
