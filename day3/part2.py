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

def is_gear(schematic, row, column):
  if row < 0 or row >= len(schematic):
    return False 
  if column < 0 or column >= len(schematic[0]):
    return False
  return schematic[row][column] == '*'

# Row and column should be of the left most digit of part number
def update_gears(schematic, gears, part_number, row, column):
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
    if is_gear(schematic, row, column):
      if row not in gears:
        gears[row] = {}
      if column not in gears[row]:
        gears[row][column] = []
      gears[row][column].append(part_number)

# Build a 2d array for the schematic
def create_schematic(input_file):
  schematic = []
  file = open(input_file, 'r')
  for line in file.readlines():
    schematic.append(line.strip())   
  return schematic

def calculate_gear_ratios(gears):
  sum = 0
  for row in gears.values():
    for part_numbers in row.values():
      if len(part_numbers) == 2:
        sum += int(part_numbers[0]) * int(part_numbers[1])
  return sum
        
def main(argv):
  input_file = argv[0]
  schematic = create_schematic(input_file)
  current_part_number = ''
  current_part_row = -1 
  current_part_column = -1
  sum = 0
  gears = {}
  for i in range(0, len(schematic)):
    if current_part_number:
      update_gears(schematic, gears, current_part_number, current_part_row, current_part_column) 
      current_part_number = ''
    for j in range(0, len(schematic[0])):
      if check_is_part_number(schematic, i, j):
        if not current_part_number:
          current_part_row = i
          current_part_column = j
        current_part_number += schematic[i][j]
        continue
      if current_part_number:  
        update_gears(schematic, gears, current_part_number, current_part_row, current_part_column) 
        current_part_number = ''
        continue
  print(calculate_gear_ratios(gears))

if __name__ == "__main__":
  main(sys.argv[1:])
