import sys

def parse_input(input_file):
  start = None
  grid = [] 
  file = open(input_file, 'r')
  for i, line in enumerate(file.readlines()):
    grid.append(line.strip())
    for j, cell in enumerate(line):
      if cell == 'S':
        start = (i, j) 
  return start[0], start[1], grid

CAN_GO_NORTH = ['S', 'J', 'L', '|']
CAN_GO_SOUTH = ['S', '7', 'F', '|']
CAN_GO_EAST = ['S', 'L', 'F', '-']
CAN_GO_WEST = ['S', 'J', '7', '-']

def can_go_north(x, y, grid):
  return x > 0 and grid[x][y] in CAN_GO_NORTH and grid[x-1][y] in CAN_GO_SOUTH

def can_go_south(x, y, grid):
  return x < len(grid)-1 and grid[x][y] in CAN_GO_SOUTH and grid[x+1][y] in CAN_GO_NORTH

def can_go_east(x, y, grid):
  return y < len(grid[0])-1 and grid[x][y] in CAN_GO_EAST and grid[x][y+1] in CAN_GO_WEST

def can_go_west(x, y, grid):
  return y > 0 and grid[x][y] in CAN_GO_WEST and grid[x][y-1] in CAN_GO_EAST

def is_parent(parents, child, parent):
  if child not in parents:
    return False 
  return parent == parents[child]
    

def bfs_helper(x, y, grid, visited, parents):
  to_visit = [(x, y)] 
  while to_visit:
    node = to_visit.pop(0)
    x = node[0]
    y = node[1]
    if x in visited and y in visited[x]:
      continue 
    if x not in visited:
      visited[x] = {}
    visited[x][y] = True 
    if can_go_north(x, y, grid) and not is_parent(parents, (x-1, y), (x, y)):
      to_visit.append((x-1, y))
      parents[(x-1, y)] = (x, y)
    if can_go_south(x, y, grid) and not is_parent(parents, (x+1, y), (x, y)):
      to_visit.append((x+1, y))
      parents[(x+1, y)] = (x, y)
    if can_go_east(x, y, grid) and not is_parent(parents, (x, y+1), (x, y)):
      to_visit.append((x, y+1))
      parents[(x, y+1)] = (x, y)
    if can_go_west(x, y, grid) and not is_parent(parents, (x, y-1), (x, y)):
      to_visit.append((x, y-1))
      parents[(x, y-1)] = (x, y)

def get_cycle(starting_points, parents):
  point1 = starting_points[0]
  point2 = starting_points[1]
  path = [point1, point2] 
  while (point1 != point2):
    point1 = parents[point1]
    point2 = parents[point2]
    if point1 == point2:
      path.append(point1)
    else:
      path.extend([point1, point2])
  return path

def get_edge_graph(grid, cycle):
  graph = [[False]*(len(grid[0])*2-1) for i in range(0, (len(grid)*2-1))]
  for x, y in cycle:
    graph[x*2][y*2] = True
    if can_go_north(x, y, grid):
      graph[x*2-1][y*2] = True
    if can_go_south(x, y, grid):
      graph[x*2+1][y*2] = True
    if can_go_east(x, y, grid):
      graph[x*2][y*2+1] = True
    if can_go_west(x, y, grid):
      graph[x*2][y*2-1] = True
  return graph

def get_flood_graph(edge_graph):
  total_num_nodes = len(edge_graph) * len(edge_graph[0])
  flood_graph = [[False] * (len(edge_graph[0])) for i in range(0, len(edge_graph))]
  visited = flood_graph.copy()
  to_visit = []
  visited_count = 0
  for i in range(0, len(edge_graph)):
    if not i == 0 and not i == len(edge_graph) - 1:
      to_visit.append((i, 0))
      to_visit.append((i, len(edge_graph[0])-1))
      continue
    for j in range(0, len(edge_graph[0])):
      to_visit.append((i, j))
  to_visit = list(filter(lambda x: not edge_graph[x[0]][x[1]], to_visit))
  while to_visit:
    node = to_visit.pop(0)
    x, y = node
    if visited[x][y]:
      continue
    visited_count += 1
    visited[node[0]][node[1]] = True
    next_nodes = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for next_node in next_nodes:
      if next_node[0] < 0 or next_node[0] >= len(edge_graph):
        continue
      if next_node[1] < 0 or next_node[1] >= len(edge_graph[0]):
        continue
      if visited[next_node[0]][next_node[1]]:
        continue
      if edge_graph[next_node[0]][next_node[1]]:
        continue
      to_visit.append(next_node)
  return flood_graph

def count_tiles(joined_graph):
  count = 0
  for i in range(0, len(joined_graph), 2):
    for j in range(0, len(list(joined_graph[i])), 2):
      if not joined_graph[i][j]:
        count += 1
  print(count) 

def pretty_print(grid):
  for row in grid:
    print('\t'.join(list(map(str, row))))

def main(argv):
  x, y, grid = parse_input(argv[0])
  distances = {}
  visited = {}
  parents = {}
  starting_points = []
  # BFS to find nodes that are in loop
  if can_go_north(x, y, grid):
    starting_points.append((x-1, y))
  if can_go_south(x, y, grid):
    starting_points.append((x+1, y))
  if can_go_east(x, y, grid):
    starting_points.append((x, y+1))
  if can_go_west(x, y, grid):
    starting_points.append((x, y-1))
  bfs_helper(x, y, grid, visited, parents)

  # Generate loop from BFS parent results
  print("Finding cycles")
  cycle = [(x, y)] + get_cycle(starting_points, parents)
  print("Building edge graph")
  edge_graph = get_edge_graph(grid, cycle)
  print("Building flood graph") 
  flood_graph = get_flood_graph(edge_graph)
  print("Joining graphs")
  joined_graph = [list(map(lambda x: x[0] or x[1], zip(*t))) for t in zip(edge_graph, flood_graph)]
  count_tiles(joined_graph)

if __name__ == "__main__":
  main(sys.argv[1:])
