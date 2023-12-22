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

def setup_djikstra(input):
  unvisited = [] 
  visited = [] 
  distances = [] 
  for i, row in enumerate(input):
    distances.append([]) 
    visited.append([])
    for j, cell in enumerate(row):
      visited[i].append(False)
      if cell == 'S':
        distances[i].append(0)
        heapq.heappush(unvisited, (0, i, j))
      else:
        distances[i].append(999)
        heapq.heappush(unvisited, (sys.maxsize, i, j))
  return visited, unvisited, distances

def build_reachable(input):
  visited, unvisited, distances = setup_djikstra(input)
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

def count_reachable(distances, max_steps):
  count = 0
  for row in distances:
    for cell in row:
      if cell <= max_steps and cell%2==0:
        count += 1
  print(count)

def main(argv):
  input = get_input(argv[0])
  distances = build_reachable(input)
  count_reachable(distances, 64)
  min_steps = 999
  min_i = 0
  min_j = 0
  for i in range(0, len(distances)):
    for j in range(0, len(distances[0])):
      #if j == 0:
      #if j == len(distances[0])-1:
      #if i == 0:
      if i == len(distances)-1:
        if distances[i][j] < min_steps:
          min_steps = distances[i][j] 
          min_i = i
          min_j = j
  pretty_print(distances)
  print(len(input), len(input[0]))
  print(min_i, min_j, min_steps)

if __name__ == "__main__":
  main(sys.argv[1:])
