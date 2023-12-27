import sys
import itertools
from common.perf import profiler
from common.grid import get_shortest_paths
from common.io import get_2d_string_input, pretty_print

def find_entry_points(grid):
  for i, row in enumerate(grid):
    for j, cell in enumerate(row):
      if cell.isdigit():
        yield (cell, i, j)

def check_permutations(entry_points, shortest):
  part1 = sys.maxsize
  part2 = sys.maxsize
  for permutation in itertools.permutations(list(filter(lambda x: x != '0', map(lambda x: x[0], entry_points)))):
    sum = 0
    for (i, j) in itertools.pairwise(['0']+list(permutation)):
      sum += shortest[(i, j)]
    part1 = min(part1, sum)
    part2 = min(part2, sum + shortest[(j, '0')])
  print('Part 1: ', part1)
  print('Part 2: ', part2)
    

@profiler
def main(argv):
  input = get_2d_string_input(argv[0])
  shortest = {}
  entry_points = list(find_entry_points(input))
  distances = get_shortest_paths(input, 1, 3)
  for c, x, y in entry_points: 
    distances = get_shortest_paths(input, x, y)
    for d, i, j in entry_points:
      if c == d:
        continue
      shortest[(c, d)] = distances[i][j]
  check_permutations(entry_points, shortest)

if __name__ == "__main__":
  main(sys.argv[1:])
