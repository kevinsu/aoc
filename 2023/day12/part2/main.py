import sys

cache = {}

def expand_line(line):
    row, groups_string = line.split()
    arrangements = groups_string.split(',')*5
    rows = [row]*5
    return "?".join(rows)+" "+",".join(arrangements)

def count_arrangements(line):
    row, groups_string = line.split()
    groups = list(map(int, groups_string.split(',')))
    return count_helper(row, groups, '')

def can_match(row, group):
    if len(row) < group:
        return False
    if any(x == '.' for x in row[0:group]):
        return False
    if len(row) == group:
        return True
    return row[group] == '.' or row[group] == '?'

def get_key(row, groups):
    return row + ' ' + ','.join(list(map(str, groups)))

def cache_and_return(key, sum):
    cache[key] = sum
    return sum

def count_helper(row, groups, layout):
    key = get_key(row,groups)
    if key in cache:
      return cache[key]
    if not row and not groups:
        return cache_and_return(key, 1) 
    if not row and groups:
        return cache_and_return(key, 0) 
    if not groups:
        if any(x == '#' for x in row):
            return cache_and_return(key, 0)
        return cache_and_return(key, 1)
   
    group = groups[0]
    if len(row) < group:
        return cache_and_return(key, 0)
    if row[0] == '.':
        layout += '.'
        return cache_and_return(key, count_helper(row[1:], groups, layout))
    match = can_match(row, group)
    if row[0] == '#':
        if match:
            layout += '#'*group+'.'
            return cache_and_return(key, count_helper(row[group + 1:], groups[1:], layout))
        return cache_and_return(key, 0) 
    if match:
        return cache_and_return(key, count_helper(row[group+1:], groups[1:], layout + '#'*group + '.') + count_helper(row[1:], groups, layout + '.'))
    layout += '.'
    return cache_and_return(key, count_helper(row[1:], groups, layout))

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    count = count_arrangements(expand_line(line)) 
    sum += count
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
