import sys
from common.output import pretty_print

def get_next_tiles(diagram, from_x, from_y, x, y):
  # From the north
  if from_x < x:
    if diagram[x][y] == '.':
      return [(x+1, y)]
    elif diagram[x][y] == '|':
      return [(x+1, y)]
    elif diagram[x][y] == '-':
      return [(x, y+1), (x, y-1)]
    elif diagram[x][y] == '\\':
      return [(x, y+1)]
    elif diagram[x][y] == '/':
      return [(x, y-1)]
    else:
      raise Exception('Bad tile: %s' % diagram[x][y])
  # From the south
  elif from_x > x:
    if diagram[x][y] == '.':
      return [(x-1, y)]
    elif diagram[x][y] == '|':
      return [(x-1, y)]
    elif diagram[x][y] == '-':
      return [(x, y+1), (x, y-1)]
    elif diagram[x][y] == '\\':
      return [(x, y-1)]
    elif diagram[x][y] == '/':
      return [(x, y+1)]
    else:
      raise Exception('Bad tile: %s' % diagram[x][y])
  # From the east
  elif from_y > y:
    if diagram[x][y] == '.':
      return [(x, y-1)]
    elif diagram[x][y] == '|':
      return [(x+1, y), (x-1, y)]
    elif diagram[x][y] == '-':
      return [(x, y-1)]
    elif diagram[x][y] == '\\':
      return [(x-1, y)]
    elif diagram[x][y] == '/':
      return [(x+1, y)]
    else:
      raise Exception('Bad tile: %s' % diagram[x][y])
  # From the west
  elif from_y < y:
    if diagram[x][y] == '.':
      return [(x, y+1)]
    elif diagram[x][y] == '|':
      return [(x+1, y), (x-1, y)]
    elif diagram[x][y] == '-':
      return [(x, y+1)]
    elif diagram[x][y] == '\\':
      return [(x+1, y)]
    elif diagram[x][y] == '/':
      return [(x-1, y)]
    else:
      raise Exception('Bad tile: %s' % diagram[x][y])
  else:
    raise Exception("from_x, from_y matches x, y")
   
def fire_laser(diagram, energized, visited, next_lasers):
  while next_lasers:
    next_laser = next_lasers.pop() 
    if next_laser[0] != -1:
      energized[next_laser[2]][next_laser[3]] += 1
    if next_laser in visited:
      continue
    visited[next_laser] = True
    next_tiles = get_next_tiles(diagram, *next_laser)
    for tile in next_tiles:
      if tile[0] < 0 or tile[0] >= len(diagram) or tile[1] < 0 or tile[1] >= len(diagram[0]):
        continue
      next_lasers.append((next_laser[2], next_laser[3], tile[0], tile[1]))
    
def count_tiles(energized):
  sum = 0
  for row in energized:
    for col in row:
      if col > 0:
        sum += 1 
  return sum

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  diagram = [[c for c in line.strip()] for line in file.readlines()]
  max_tiles = 0
  for i in range(0, len(diagram)):
    energized = [[0]*len(diagram[0]) for row in diagram]
    fire_laser(diagram, energized, {}, [(i, -1, i, 0)])
    max_tiles = max(max_tiles, count_tiles(energized))

    energized = [[0]*len(diagram[0]) for row in diagram]
    fire_laser(diagram, energized, {}, [(i, len(diagram[0]), i, len(diagram[0])-1)])
    max_tiles = max(max_tiles, count_tiles(energized))
  for j in range(0, len(diagram[0])):
    energized = [[0]*len(diagram[0]) for row in diagram]
    fire_laser(diagram, energized, {}, [(-1, j, 0, j)])
    max_tiles = max(max_tiles, count_tiles(energized))

    energized = [[0]*len(diagram[0]) for row in diagram]
    fire_laser(diagram, energized, {}, [(len(diagram), j, len(diagram)-1, j)])
    max_tiles = max(max_tiles, count_tiles(energized))
  print(max_tiles)
if __name__ == "__main__":
  main(sys.argv[1:])
