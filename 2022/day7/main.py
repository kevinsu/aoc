import sys

def is_dir_ready(dirs, dir, done):
  for item in dirs[dir]:
    if item.startswith('dir'):
      name = item.split()[1]
      full_dir = '/'.join([dir, name])
      if full_dir in done:
        continue
      return False
  return True

def calculate_dir_size(dir, contents, done):
  sum = 0
  for item in contents:
    item_split = item.split()
    if item.startswith('dir'):
      full_dir = '/'.join([dir, item_split[1]])
      sum += done[full_dir]
    else:
      sum += int(item_split[0]) 
  return sum

def get_parent(dir):
  if len(dir) <= 1:
    return None
  return '/'.join(dir.split('/')[0:-1])

def calculate_dir_sizes(dirs):
  done = {}
  not_done = dirs.keys() 
  next_dirs = []
  for dir, contents in dirs.items():
    if is_dir_ready(dirs, dir, done):
      next_dirs.append(dir)
  while next_dirs:
    dir = next_dirs.pop() 
    done[dir] = calculate_dir_size(dir, dirs[dir], done)
    parent = get_parent(dir)
    if parent and is_dir_ready(dirs, parent, done):
      next_dirs.append(parent)
  sum = 0
  for key, value in done.items():
    if value < 100000:
      sum += value
  print(sum)
  return done
 
def get_dirs(input_file):
  file = open(input_file, 'r')
  stack = []
  dirs = {}
  for line in file.readlines():
    if line.startswith('$ cd'):
      current_dir = line.split()[2]
      if current_dir == '..':
        current_dir = stack.pop()
      else:
        stack.append(current_dir)
        full_dir = '/'.join(stack)
        if full_dir not in dirs:
          dirs[full_dir] = []
      is_listing = False
      continue
    if line.startswith('$ ls'):
      is_listing = True
      continue
    if is_listing:
      full_dir = '/'.join(stack)
      dirs[full_dir].append(line.strip())
  return dirs

def get_delete_dir(done):
  total = 70000000
  free = total - done['/']
  needed = 30000000 - free
  current = total
  for size in done.values():
    if size > needed:
      current = min(current, size) 
  print(current)
  
def main(argv):
  dirs = get_dirs(argv[0])
  done = calculate_dir_sizes(dirs)
  get_delete_dir(done)

if __name__ == "__main__":
  main(sys.argv[1:])
