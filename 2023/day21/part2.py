import sys
import math
import heapq
from common.io import get_2d_string_input as get_input 
from common.io import pretty_print
from common.perf import profiler

def get_adjacent(input, i, j):
  if i-1 >= 0 and input[i-1][j] != '#':
    yield (i-1, j)
  if i+1 < len(input) and input[i+1][j] != '#':
    yield (i+1, j)
  if j-1 >= 0 and input[i][j-1] != '#':
    yield (i, j-1)
  if j+1 < len(input[0]) and input[i][j+1] != '#':
    yield (i, j+1)

def setup_djikstra(input, start_x, start_y):
  unvisited = [] 
  visited = [] 
  distances = [] 
  for i, row in enumerate(input):
    distances.append([]) 
    visited.append([])
    for j, cell in enumerate(row):
      visited[i].append(False)
      if (i, j) == (start_x, start_y): 
        distances[i].append(0)
        heapq.heappush(unvisited, (0, i, j))
      else:
        distances[i].append(sys.maxsize)
        heapq.heappush(unvisited, (sys.maxsize, i, j))
  return visited, unvisited, distances

def get_distances(input, start_x, start_y):
  visited, unvisited, distances = setup_djikstra(input, start_x, start_y)
  while unvisited:
    distance, i, j = heapq.heappop(unvisited)
    if visited[i][j]:
      continue
    visited[i][j] = True 
    for x, y in get_adjacent(input, i, j):
      tentative = distances[i][j]+1
      if tentative < distances[x][y]: 
        distances[x][y] = tentative 
        heapq.heappush(unvisited, (tentative, x, y))
  return distances

def get_start(input):
  for i, row in enumerate(input):
    for j, cell in enumerate(row):
      if cell == 'S':
        return (i, j)
        
def build_all_shortest_paths(input, input_start):
  all_shortest_paths = {}
  # Get 4 corners and 4 middles and start
  starts = [input_start, (0, 0), (0, len(input[0])-1), (len(input)-1, 0), (len(input)-1, len(input[0])-1), (0, int(len(input[0])/2)), (len(input)-1, int(len(input[0])/2)), (int(len(input)/2), 0), (int(len(input)/2), len(input[0])-1)]
  for start in starts:
    if start[0] not in all_shortest_paths:
      all_shortest_paths[start[0]] = {}
    all_shortest_paths[start[0]][start[1]] = get_distances(input, *start) 
  return all_shortest_paths

def count_quadrant(distances, steps_left, grid_size, start_x, start_y):
  if steps_left < 0:
    return 0
  target_steps = grid_size * 3 
  full_grid_count = 0
  if steps_left >= target_steps:
    full_grid_count = int((steps_left - target_steps)/ grid_size)
    steps_left = steps_left - full_grid_count*grid_size
  num_grids = full_grid_count+1
  full_grid_even = count_reachable(distances, sys.maxsize, 0)
  full_grid_odd = count_reachable(distances, sys.maxsize, 1)
  sum = 0
  even = full_grid_count%2 == 0
  if even: 
    num_odd = (full_grid_count*(full_grid_count+1)/2 - math.ceil(full_grid_count/2))/2
    num_even = full_grid_count*(full_grid_count+1)/2 - num_odd
    sum = full_grid_odd * num_odd + full_grid_even * num_even
  else:
    num_even = (full_grid_count * (full_grid_count+1) /2 - math.ceil(full_grid_count/2))/2
    num_odd = full_grid_count *(full_grid_count +1) /2 - num_even
    sum = full_grid_odd * num_odd + full_grid_even * num_even  
  while steps_left > 0:
    count = count_reachable(distances, steps_left, 1 if even else 0)
    sum += count*num_grids
    num_grids += 1
    steps_left -= grid_size
    even = not even
  return sum

def count_cardinal(distances, steps_left, grid_size, start_x, start_y):
  if steps_left < 0:
    return 0 
#  if steps_left == 0:
#    return count_reachable(distances, 1)
  target_steps = grid_size * 3 
  full_grid_count = 0
  if steps_left >= target_steps:
    full_grid_count = int((steps_left - target_steps)/ grid_size)
    steps_left = steps_left - full_grid_count*grid_size
  full_grid_even = count_reachable(distances, sys.maxsize, 0)
  full_grid_odd = count_reachable(distances, sys.maxsize, 1)
  even = full_grid_count %2 == 0
  sum = 0
  if even:
    sum = (full_grid_even+full_grid_odd) * full_grid_count/2
  else:
    sum = full_grid_odd * int(full_grid_count/2+1)+full_grid_even*int(full_grid_count)
  while steps_left >= 0:
    count = count_reachable(distances, steps_left, 1 if even else 0)
    sum += count
    steps_left -= grid_size
    even = not even
  return sum
    
def count_reachable(distances, max_steps, remainder):
  count = 0
  for row in distances:
    for cell in row:
      if cell <= max_steps and cell != sys.maxsize and cell%2 == remainder:
        count += 1
  return count

def triple_input(input):
  result = []
  for i in range(0, 3):
    for row in input:
      result.append(row*3) 
  return result
      
@profiler
def main(argv):
  input = get_input(argv[0])
  total_steps = int(argv[1])
  start_x, start_y = get_start(input)
  max_x = len(input)-1
  max_y = len(input[0])-1
  mid_x = int(len(input)/2)
  mid_y = int(len(input[0])/2)
  sum = 0

  all_shortest_paths = build_all_shortest_paths(input, (start_x, start_y))
  start_sum = count_reachable(all_shortest_paths[start_x][start_y], total_steps, 1)

  steps_to_upper_right = all_shortest_paths[start_x][start_y][0][max_y]
  upper_right_sum = count_quadrant(all_shortest_paths[max_x][0], total_steps - steps_to_upper_right-2, len(input), 1, 1)

  steps_to_bottom_right = all_shortest_paths[start_x][start_y][max_x][max_y]
  bottom_right_sum = count_quadrant(all_shortest_paths[0][0], total_steps - steps_to_bottom_right-2, len(input), 1, -1)

  steps_to_bottom_left = all_shortest_paths[start_x][start_y][max_x][0]
  bottom_left_sum = count_quadrant(all_shortest_paths[0][max_y], total_steps - steps_to_bottom_left-2, len(input), -1, -1)

  steps_to_upper_left = all_shortest_paths[start_x][start_y][0][0]
  upper_left_sum = count_quadrant(all_shortest_paths[max_x][max_y], total_steps - steps_to_upper_left-2, len(input), -1, 1)

  steps_to_up = all_shortest_paths[start_x][start_y][0][mid_y]
  up_sum = count_cardinal(all_shortest_paths[max_x][mid_y], total_steps - steps_to_up-1, len(input), 0, 1)

  steps_to_right = all_shortest_paths[start_x][start_y][mid_x][max_y]
  right_sum = count_cardinal(all_shortest_paths[mid_x][0], total_steps - steps_to_right-1, len(input), 1, 0)

  steps_to_down = all_shortest_paths[start_x][start_y][max_x][mid_y]
  down_sum = count_cardinal(all_shortest_paths[0][mid_y], total_steps - steps_to_down-1, len(input), 0, -1)

  steps_to_left = all_shortest_paths[start_x][start_y][mid_x][0]
  left_sum = count_cardinal(all_shortest_paths[mid_x][max_y], total_steps - steps_to_left-1, len(input), -1, 0)
  reachable = 0
  unreachable = 0
  total = 0
  print("result: ", up_sum + upper_right_sum + start_sum + right_sum + bottom_right_sum + down_sum + bottom_left_sum + left_sum + upper_left_sum)

if __name__ == "__main__":
  main(sys.argv[1:])
