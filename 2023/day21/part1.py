import sys
import heapq
from common.io import get_2d_string_input as get_input 
from common.io import pretty_print

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

def count_reachable(distances, max_steps, remainder):
  count = 0
  for row in distances:
    for cell in row:
      if cell <= max_steps and cell != sys.maxsize and cell%2==remainder:
        count += 1
  return count

def get_start(input):
  for i, row in enumerate(input):
    for j, cell in enumerate(row):
      if cell == 'S':
        return (i, j)

def main(argv):
  input = get_input(argv[0])
  start_x, start_y = get_start(input)
  distances = get_distances(input, start_x, start_y)
  print(count_reachable(distances, 64, 0))

if __name__ == "__main__":
  main(sys.argv[1:])
