import sys

def check_is_part_number(schematic, row, column):
  if row < 0 or row >= len(schematic):
    return False 
  if column < 0 or column >= len(schematic[0]):
    return False
  try:
    int(schematic[row][column])
    return True
  except:
    return False

def is_symbol(schematic, row, column):
  if row < 0 or row >= len(schematic):
    return False 
  if column < 0 or column >= len(schematic[0]):
    return False
  if schematic[row][column] == '.':
    return False 
  try:
    int(schematic[row][column])
    return False
  except:
    return True
     

# Row and column should be of the left most digit of part number
def has_adjacent_symbol(schematic, row, column):
  to_check = []
  to_check.append((row-1, column-1)) 
  to_check.append((row, column-1))
  to_check.append((row+1, column-1))   
  is_part_number = True
  while (is_part_number):
    to_check.append((row-1, column))
    to_check.append((row+1, column))
    column += 1
    is_part_number = check_is_part_number(schematic, row, column)   
  to_check.append((row-1, column))   
  to_check.append((row, column))  
  to_check.append((row+1, column))   
  for row, column in to_check:
    if is_symbol(schematic, row, column):
      return True 
  
  return False

# Build a 2d array for the schematic
def create_schematic(input_file):
  schematic = []
  file = open(input_file, 'r')
  for line in file.readlines():
    schematic.append(line.strip())   
  return schematic

def process(schematic, part_number, row, column):
  if has_adjacent_symbol(schematic, row, column):
    return int(part_number)
  return 0

def main(argv):
  input_file = argv[0]
  schematic = create_schematic(input_file)
  current_part_number = ''
  current_part_row = -1 
  current_part_column = -1
  sum = 0
  for i in range(0, len(schematic)):
    if current_part_number:
      sum += process(schematic, current_part_number, current_part_row, current_part_column) 
      current_part_number = ''
    for j in range(0, len(schematic[0])):
      if check_is_part_number(schematic, i, j):
        if not current_part_number:
          current_part_row = i
          current_part_column = j
        current_part_number += schematic[i][j]
        continue
      if current_part_number:  
        sum += process(schematic, current_part_number, current_part_row, current_part_column) 
        current_part_number = ''
        continue
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
