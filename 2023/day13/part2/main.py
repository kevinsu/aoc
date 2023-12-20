import sys
import itertools

def find_symmetry(l, existing_line):
  for i in range(1, len(l)):
    if i == existing_line:
      continue
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

def get_patterns(input_file):
  file = open(input_file, 'r')
  patterns = []
  pattern = []
  for line in file.readlines():
    if line == '\n':
      patterns.append(pattern)
      pattern = []
      continue
    pattern.append(line.strip())
  patterns.append(pattern)
  return patterns

def pretty_print(array):
  for row in array:
    line = []
    for cell in row:
      line.append(cell)
    print(" ".join(line))

def get_sums(pattern):
  rows = [0]*len(pattern)
  columns = [0]*len(pattern[0])
  for i, row in enumerate(pattern):
    for j, column in enumerate(row):
      if column == '#':
        rows[i] += 2**(j)
        columns[j] += 2**(i)
  return rows, columns 

def find_new_symmetry(pattern, rows, columns):
  row_symmetry = find_symmetry(rows, 0)
  column_symmetry = find_symmetry(columns, 0)
  for i, row in enumerate(pattern):
    for j, column in enumerate(row):
      copy_rows = rows.copy()
      copy_columns = columns.copy()
      if column == '#':
        copy_rows[i] -= 2**j 
        copy_columns[j] -= 2**i
      else:
        copy_rows[i] += 2**j 
        copy_columns[j] += 2**i
      copy_row_symmetry = find_symmetry(copy_rows, row_symmetry)
      copy_column_symmetry = find_symmetry(copy_columns, column_symmetry)
      if (copy_row_symmetry != row_symmetry and copy_row_symmetry != 0) or (copy_column_symmetry!= column_symmetry and copy_column_symmetry != 0):
        return copy_row_symmetry, copy_column_symmetry, row_symmetry, column_symmetry, i, j
  return 0, 0, -1, -1, -1, -1
      
        

def main(argv):
  patterns = get_patterns(argv[0])
  sum = 0
  for pattern in patterns:
    rows, columns = get_sums(pattern)
    row_symmetry, column_symmetry, original_row_symmetry, original_column_symmetry,i, j = find_new_symmetry(pattern, rows, columns)
    sum += row_symmetry * 100 + column_symmetry
  print(sum)
    

def main_old(argv):
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
  row_index = find_symmetry(columns)
  col_index = find_symmetry(rows)
  sum += row_index + col_index * 100
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
