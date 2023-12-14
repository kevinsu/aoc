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

def get_map_key(rock_map):
  return ''.join([''.join(row) for row in rock_map])

def run_cycle(rock_map):
  west_facing = get_map_tilted_north_facing_west(rock_map)
  south_facing = get_map_tilted_north_facing_west(west_facing)
  east_facing = get_map_tilted_north_facing_west(south_facing)
  north_facing = get_map_tilted_north_facing_west(east_facing)
  return north_facing

def get_map_tilted_north_facing_west(rock_map):
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
    north_map.append(list(reversed(column))) 
  return north_map 

def get_map_value(m):
  sum = 0
  for i, row in enumerate(reversed(m)):
    sum += row.count('O') * (i + 1) 
  return sum

def get_largest_multiple_with_mod_under_max(multiple, mod, max):
  candidate = int(max / multiple) * multiple + mod
  while candidate > max:
    candidate -= multiple
  return candidate

NUM_CYCLES = 1000000000
def run_cycles(rock_map):
  cache = {}
  current_map = rock_map
  i = 0
  skipped = False
  while i < NUM_CYCLES:
    key = get_map_key(current_map)
    if key in cache:
      current_map, first_seen = cache[key]  
      if not skipped:
        i = get_largest_multiple_with_mod_under_max(i - first_seen, first_seen, NUM_CYCLES)
        skipped = True
      i+= 1
      continue
    current_map = run_cycle(current_map)
    if key not in cache:
      cache[key] = (current_map, i)
    i+=1
  return current_map

def main(argv):
  rock_map = get_rock_map(argv[0])
  result = run_cycles(rock_map)
  print(get_map_value(result))

if __name__ == "__main__":
  main(sys.argv[1:])
