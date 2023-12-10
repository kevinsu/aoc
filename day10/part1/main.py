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

def dfs_helper(x, y, grid, path, visited):
  if len(path) > 2 and grid[x][y] == 'S': 
    return True, path
  new_path = path.copy()
  new_path.append((x, y)) 
  if x in visited and y in visited[x]:
    return False, path
  new_visited = visited.copy()
  if x not in new_visited:
    new_visited[x] = {}
  new_visited[x][y] = True
  finished = False
  result = []
  if can_go_north(x, y, grid):
    finished, result = dfs_helper(x-1, y, grid, new_path, new_visited)
  if not finished and can_go_south(x, y, grid):
    finished, result = dfs_helper(x+1, y, grid, new_path, new_visited)
  if not finished and can_go_east(x, y, grid):
    finished, result = dfs_helper(x, y+1, grid, new_path, new_visited)  
  if not finished and can_go_west(x, y, grid):
    finished, result = dfs_helper(x, y-1, grid, new_path, new_visited)
  return finished, result

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
    print('to_visit: ', to_visit)

def count_steps(starting_points, parents):
  point1 = starting_points[0]
  point2 = starting_points[1]
  steps = 0
  while (point1 != point2):
    print(point1)
    print(point2)
    steps+= 1
    point1 = parents[point1]
    point2 = parents[point2]
  return steps

def get_distances(x, y, grid):
  distances = {}
  visited = {}
  parents = {}
  starting_points = []
  if can_go_north(x, y, grid):
    starting_points.append((x-1, y))
  if can_go_south(x, y, grid):
    starting_points.append((x+1, y))
  if can_go_east(x, y, grid):
    starting_points.append((x, y+1))
  if can_go_west(x, y, grid):
    starting_points.append((x, y-1))
  bfs_helper(x, y, grid, visited, parents)
  print(parents)
  print(count_steps(starting_points, parents)+1)

def main(argv):
  x, y, grid = parse_input(argv[0])
  get_distances(x, y, grid)

if __name__ == "__main__":
  main(sys.argv[1:])
