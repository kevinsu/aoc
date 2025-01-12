import sys
import sympy as sp
from common.perf import profiler

def eval(monkeys, name):  
  if isinstance(monkeys[name], int):
    return monkeys[name]
  left, op, right = monkeys[name].split()
  result = None
  if op == '+':
    result = eval(monkeys, left) + eval(monkeys, right)    
  elif op == '-':
    result = eval(monkeys, left) - eval(monkeys, right)    
  elif op == '/':
    result = eval(monkeys, left) / eval(monkeys, right)
  elif op == '*':
    result = eval(monkeys, left) * eval(monkeys, right)
  if not result:
    raise Exception
  monkeys[name] = result
  return result

def eval_x(monkeys, name):  
  if isinstance(monkeys[name], int):
    return monkeys[name]  
  if isinstance(monkeys[name], sp.Expr):
    return monkeys[name]  
  left, op, right = monkeys[name].split()
  left_side = left
  right_side = right
  if left == 'humn':
    left_side = sp.Symbol('x')
  else:
    left_side = eval_x(monkeys, left)
  if right == 'humn':  
    right_side = sp.Symbol('x')
  else:
    right_side = eval_x(monkeys, right)
  if op == '+':
    return left_side + right_side
  elif op == '-':
    return left_side - right_side
  elif op == '/':
    return left_side / right_side
  elif op == '*':
    return left_side * right_side
  else:
    raise Exception
  
def part1(monkeys):
  return eval(monkeys, 'root')

def part2(monkeys):
  left, _, right = monkeys['root'].split()

  left = eval_x(monkeys, left)
  right = eval_x(monkeys, right)
  solution = sp.Eq(left, right)
  x = sp.Symbol('x')
  solution = sp.solve(solution, (x))
  return solution[0]
  
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  monkeys = {}
  for line in file.readlines():
    key, value = line.split(':')
    try:
      monkeys[key] = int(value)
    except:
      monkeys[key] = value.strip()
  print(part1(monkeys.copy()))
  print(part2(monkeys))

if __name__ == "__main__":
  main(sys.argv[1:])
