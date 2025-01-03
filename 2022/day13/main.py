import ast
from functools import cmp_to_key
import sys
from common.perf import profiler
from itertools import zip_longest

def in_order(left, right):
  #print('in_order: ', left, right)
  for l, r in zip_longest(left, right, fillvalue=None):
    result = None
    if l == None:
      return True
    if r == None:
      return False
    if isinstance(l, int) and isinstance(r, int):
       if l > r:
          return False
       elif l < r:
          return True
    elif isinstance(l, int):
       result = in_order([l], r)
    elif isinstance(r, int):
       result = in_order(l, [r])
    else:
       result = in_order(l, r)

    if result != None:
       return result

def part1(pairs):
  sum = 0
  for i, pair in enumerate(pairs):
    left, right = pair.split()
    if in_order(ast.literal_eval(left), ast.literal_eval(right)):
      sum += i+1
  return sum

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

def part2(pairs):
  l = [[[2]], [[6]]]
  for pair in pairs:
    left, right = pair.split()
    l.append(ast.literal_eval(left))
    l.append(ast.literal_eval(right))
  product = 1
  for i, item in enumerate(sorted(l,key=cmp_to_key(make_comparator(in_order)))):
     if item in [[[2]], [[6]]]:
        product = product * (i+1)

  return product
           
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  pairs = file.read().split('\n\n')
  #print(part1(pairs))
  print(part2(pairs))

if __name__ == "__main__":
  main(sys.argv[1:])
