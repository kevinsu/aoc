import sys
import heapq as heap
import common.io as io 

# Returns (x, y, is_straight)
def get_adjacent_blocks(grid, x, y, previous_x, previous_y, counter):
  if previous_x == -1:
    return [(0, 1, 0, 0, 1), (1, 0, 0, 0, 1)]
  north = (x-1, y)
  south = (x+1, y)
  east = (x, y+1)
  west = (x, y-1)
  blocks = []
  previous = (previous_x, previous_y)
  opposite_previous = (2*x-previous_x, 2*y-previous_y)
  blocks = []
  for block in [north, south, east, west]:
    if block[0] < 0 or block[0] >= len(grid):
      continue
    if block[1] < 0 or block[1] >= len(grid[0]):
      continue
    if block == previous:
      continue
    is_straight = block == opposite_previous
    if counter < 4 and not is_straight:
      continue
    if counter == 10 and is_straight:
      continue
    new_counter = counter + 1 if is_straight else 1
    blocks.append(block+(x, y)+(new_counter,))
  return blocks

def pretty_print(distances):
  for row in distances:
    print(' '.join(list(map(lambda x: str(x[0]), row))))

def get_key(x, y, previous_x, previous_y, counter):
  return '%d:%d:%d:%d:%d' % (x, y, previous_x, previous_y, counter)

def get_unvisited_options(grid, x, y):
  north = (x-1, y)
  south = (x+1, y)
  east = (x, y+1)
  west = (x, y-1)
  blocks = []
  for block in [north, south, east, west]:
    if block[0] < 0 or block[0] >= len(grid):
      continue
    if block[1] < 0 or block[1] >= len(grid[0]):
      continue
    for counter in range(1, 11):
      blocks.append((x, y, block[0], block[1], counter))
  return blocks
  

def build_unvisited(grid):
  unvisited = []
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if i == 0 and j == 0:
        heap.heappush(unvisited, (0, 0, 0, -1, -1, 1))
        continue
      for option in get_unvisited_options(grid, i, j):
        heap.heappush(unvisited, (sys.maxsize,)+option)
  return unvisited

def get_min_distance(grid, distances):
  result = sys.maxsize
  for key,value in distances.items():
    if key.startswith('%d:%d:' % (len(grid)-1, len(grid[0])-1)):
      _, _, _, _, counter = key.split(':')
      if int(counter) >= 4:
        result = min(result, value)
  print(result)
        

def pretty_print_distances(grid, distances): 
  result = [[999999] * len(grid[0]) for row in grid] 
  for key, value in distances.items():
    x, y, _, _, _ = key.split(':')
    result[int(x)][int(y)] = min(value, result[int(x)][int(y)])
  io.pretty_print(result)

def run_shortest_path(grid):
  visited = {} 
  distances = {}
  unvisited = build_unvisited(grid) 
  key = get_key(0, 0, -1, -1, 1)
  distances[key] = 0 
  num_blocks = len(unvisited)
  done = 0
  while unvisited:
    done += 1
    if done % 100 == 0:
      print('Done %s of %s' % (done, num_blocks))
    test = heap.heappop(unvisited)
    distance, x, y, px, py, counter = test
    current_block = (x, y, px, py, counter)
    if not current_block:
      break
    current_key = get_key(*current_block)
    visited[current_key] = True
    distance = distances.get(current_key, sys.maxsize)
    adjacent_blocks = get_adjacent_blocks(grid, *current_block)
    for block in adjacent_blocks:
      adjacent_key = get_key(*block)
      if adjacent_key in visited:
        continue
      next_distance = distances.get(adjacent_key, sys.maxsize)
      tentative = distance + grid[block[0]][block[1]]
      if tentative < next_distance:
        distances[adjacent_key] = tentative 
        heap.heappush(unvisited, (tentative, *block))
  get_min_distance(grid, distances)

def main(argv):
  grid = io.get_2d_int_array_from_file(argv[0]) 
  run_shortest_path(grid)

if __name__ == "__main__":
  main(sys.argv[1:])
