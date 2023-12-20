import sys
import itertools

def find_symmetry(l):
  for i in range(1, len(l)):
    symmetric = True
    left = list(reversed(l[0:i]))
    right = l[i:]
    for j in range(0, min(len(left), len(right))):
      if left[j] != right[j]:
        symmetric = False
        break
    if symmetric:
      return i 
  return 0 

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  rows = []
  columns = []
  offset = 0
  sum = 0
  for i, line in enumerate(file.readlines()):
    if line == '\n':
      offset = i
      row_index = find_symmetry(columns)
      col_index = find_symmetry(rows)
      sum += row_index + col_index * 100
      print(rows, columns)
      rows = []
      columns = []
      continue
    if not columns:
      columns = [0] * len(line.strip())
    row_value = 0 
    for j, column in enumerate(line): 
      if column == '#':
        row_value += 2**(j)
        columns[j] += 2**(i-offset)
    rows.append(row_value)
  print(rows, columns)
  row_index = find_symmetry(columns)
  col_index = find_symmetry(rows)
  sum += row_index + col_index * 100
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
