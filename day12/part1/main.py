import sys

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
   
def count_helper(row, groups, layout):
    if not row and not groups:
        return 1
    if not row and groups:
        return 0
    if not groups:
        if any(x == '#' for x in row):
            return 0
        return 1
   
    group = groups[0]
    if len(row) < group:
        return 0
    if row[0] == '.':
        layout += '.'
        return count_helper(row[1:], groups, layout)
    match = can_match(row, group)
    if row[0] == '#':
        if match:
            layout += '#'*group+'.'
            return count_helper(row[group + 1:], groups[1:], layout)
        return 0
    if match:
        return count_helper(row[group+1:], groups[1:], layout + '#'*group + '.') + count_helper(row[1:], groups, layout + '.')
    layout += '.'
    return count_helper(row[1:], groups, layout)

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    count = count_arrangements(line) 
    sum += count
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
