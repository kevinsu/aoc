import sys
from common.perf import profiler

def get_vertices(x, y, z):
  for dx, dy, dz in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
    yield (x+dx, y+dy, z+dz)

def get_sides(x, y, z):
    # z
    yield (x, y, z, x+1, y, z, x, y+1, z, x+1, y+1, z)
    # z+1
    yield (x, y, z+1, x+1, y, z+1, x, y+1, z+1, x+1, y+1, z+1)
    # y
    yield (x, y, z, x+1, y, z, x, y, z+1, x+1, y, z+1)
    # y+1
    yield (x, y+1, z, x+1, y+1, z, x, y+1, z+1, x+1, y+1, z+1)
    # x
    yield (x, y, z, x, y+1, z, x, y, z+1, x, y+1, z+1)
    # x+1
    yield (x+1, y, z, x+1, y+1, z, x+1, y, z+1, x+1, y+1, z+1)

def part1(cubes):
  sides = {}
  for cube in cubes:
    for side in get_sides(*cube):
      if side not in sides:
        sides[side] = 0
      sides[side] += 1
  return sum(1 for value in sides.values() if value == 1)

def get_neighbors(grid, x, y, z):
  if x < len(grid)-1 and grid[x+1][y][z] == 0:
    yield x+1, y, z
  if x > 0 and grid[x-1][y][z] == 0:
    yield x-1, y, z
  if y < len(grid[0])-1 and grid[x][y+1][z] == 0:
    yield x, y+1, z
  if y > 0 and grid[x][y-1][z] == 0:
    yield x, y-1, z
  if z < len(grid[0][0])-1 and grid[x][y][z+1] == 0:
    yield x, y, z+1
  if z > 0 and grid[x][y][z-1] == 0:
    yield x, y, z-1

def part2(cubes):
  max_x = 0
  max_y = 0
  max_z = 0
  for x, y, z in cubes:
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)
  grid = [[[0]*(max_z+2) for _ in range(max_y+2)] for _ in range(max_x+2)]
  for x, y, z in cubes:
    grid[x][y][z] = 1
  visited = set()
  queue = [(0, 0, 0)]
  while queue:
    x, y, z = queue.pop()
    if (x, y, z) in visited:
      continue
    visited.add((x, y, z))
    grid[x][y][z] = 1
    queue.extend(get_neighbors(grid, x, y, z))
  
  steam = set()
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      for z in range(len(grid[0][0])):
        if grid[x][y][z] == 0:
          steam.add((x, y, z))
  return part1(cubes | steam)

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  cubes = set()
  for line in file.readlines():
    cubes.add(tuple(map(int, line.split(","))))      
  print(part1(cubes))
  print(part2(cubes))
  
if __name__ == "__main__":
  main(sys.argv[1:])

