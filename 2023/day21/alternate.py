import sys
import math
import heapq
from common.io import get_2d_string_input as get_input 
from common.io import pretty_print
from common.perf import profiler
from part2 import get_distances, count_reachable, get_start

def get_start(input):
  for i, row in enumerate(input):
    for j, cell in enumerate(row):
      if cell == 'S':
        return (i, j)

def build_all_shortest_paths(input, input_start):
  all_shortest_paths = {}
  # Get 4 corners and 4 middles and start
  starts = [(65, 65), (0, 0), (0, 130), (130, 0), (130, 130), (0, 65), (130, 65), (65, 0), (65, 130)] 
  for start in starts:
    if start[0] not in all_shortest_paths:
      all_shortest_paths[start[0]] = {}
    all_shortest_paths[start[0]][start[1]] = get_distances(input, *start) 
  return all_shortest_paths

@profiler
def main(argv):
  input = get_input(argv[0])
  #total_steps = 26501365
  total_steps = int(argv[1]) 
  start_x, start_y = get_start(input)
  all_shortest_paths = build_all_shortest_paths(input, (start_x, start_y))
  # Take the opposite end of grid when calculating shortest path, i.e. we head north and enter from south of next grid.
  north = count_reachable(all_shortest_paths[130][65], 130, 0)
  south = count_reachable(all_shortest_paths[0][65], 130, 0)
  east = count_reachable(all_shortest_paths[65][0], 130, 0)
  west = count_reachable(all_shortest_paths[65][130], 130, 0)
  big_ne = count_reachable(all_shortest_paths[130][0], 195, 1)
  big_nw = count_reachable(all_shortest_paths[130][130], 195, 1)
  big_se = count_reachable(all_shortest_paths[0][0], 195, 1)
  big_sw = count_reachable(all_shortest_paths[0][130], 195, 1)
  small_ne = count_reachable(all_shortest_paths[130][0], 64, 0)
  small_nw = count_reachable(all_shortest_paths[130][130], 64, 0)
  small_se = count_reachable(all_shortest_paths[0][0], 64, 0)
  small_sw = count_reachable(all_shortest_paths[0][130], 64, 0)
  odd_grid_steps = count_reachable(all_shortest_paths[start_x][start_y], sys.maxsize, 1)
  even_grid_steps = count_reachable(all_shortest_paths[start_x][start_y], sys.maxsize, 0)
  num_full_grids = (total_steps - 65)/131-2# total steps - steps to edge - size of grid
  # num full grids is odd
  num_even_full_grids = (num_full_grids*(num_full_grids+1)/2 - math.ceil(num_full_grids/2))/2 
  num_odd_full_grids = num_full_grids*(num_full_grids+1)/2 - num_even_full_grids
  print(num_full_grids, num_odd_full_grids, num_even_full_grids) 
  print(north, big_ne, small_ne, odd_grid_steps)

  sum = 0
  sum += north + south + east + west
  sum += (num_full_grids + 1)* (small_ne + small_nw + small_se + small_sw)
  sum += num_full_grids* (big_ne + big_nw + big_se + big_sw)
  sum += 4 * (num_even_full_grids * even_grid_steps + num_odd_full_grids*odd_grid_steps)
  sum += odd_grid_steps
  print('full grid contribution: ', 4 * (num_even_full_grids * even_grid_steps + num_odd_full_grids*odd_grid_steps))
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
