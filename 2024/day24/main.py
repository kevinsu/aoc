import random
import sys
from common.perf import profiler

def get_answer(registers):
  string = ''
  for k in sorted(filter(lambda x: x.startswith('z'), registers), reverse=True):
    string += str(registers[k])
  return int(string, 2)

def eval(registers, gates, gate_name):
  gate = gates[gate_name]
  left = None
  if gate[0] in registers:
    left = registers[gate[0]]
  else:
    left = eval(registers, gates, gate[0])
  right = None
  if gate[2] in registers:
    right = registers[gate[2]]
  else:
    right = eval(registers, gates, gate[2])
  if gate[1] == 'AND':
    registers[gate_name] = left and right
  elif gate[1] == 'XOR':
    registers[gate_name] = left ^ right
  else:
    registers[gate_name] = left or right
  return registers[gate_name]

def get_dependencies(dependencies, key, cache):
  if key in cache:
    return cache[key]
  g1, g2 = dependencies[key]
  result = set()
  if g1.startswith('x') or g1.startswith('y'):
    result = result | {g1}
  else:
    result = {g1} | get_dependencies(dependencies, g1, cache)
  if g2.startswith('x') or g2.startswith('y'):
    result = result | {g2}
  else:
    result = result | {g2} | get_dependencies(dependencies, g2, cache)
  cache[key] = result
  return result
  
def get_full_dependencies(dependencies):
  cache = {}
  for key in dependencies.keys():
    get_dependencies(dependencies, key, cache)



def part1(registers, gates):
  for gate in gates:
    eval(registers, gates, gate)
  print(get_answer(registers))

def get_cluster(names, label):
  dot = f'\tsubgraph cluster_{label} '+'{\n'
  dot += f'\t\tlabel="{label}";\n'
  for name in sorted(names):
    dot += f'\t\t{name};\n'
  dot += '\t}\n'
  #dot += '\t{\n'
  #dot += '\t\trank = same;\n'
  #dot += '\t\t' + "->".join(sorted(names)) + ";\n"
  #dot += '\t\trankdir=LR;\n'
  #dot += '\t}\n'
  return dot

def get_dot(gates):
  names = set()
  for g3, gate in gates.items():
    names.update({gate[0], gate[2], g3})
  xgates = set()
  ygates = set()
  zgates = set()
  for name in names:
    if name.startswith('z'):
      zgates.add(name)
    if name.startswith('y'):
      ygates.add(name)
    if name.startswith('x'):
      xgates.add(name)
  dot = 'digraph {\n'
  dot += get_cluster(xgates, 'x')
  dot += get_cluster(ygates, 'y')
  dot += get_cluster(zgates, 'z')
  
  for gate3, gate in gates.items():
    dot += f'\t{gate[0]} -> {gate[0]}{gate[2]} [label=\"{gate[1]}\"];\n'
    dot += f'\t{gate[2]} -> {gate[0]}{gate[2]} [label=\"{gate[1]}\"];\n'
    dot += f'\t{gate[0]}{gate[2]} [label=\"{gate[1]}\"];\n'
    dot += f'\t{gate[0]}{gate[2]} -> {gate3};\n'
  dot += '}\n'
  return dot

def simulate(x, y, gates, dependencies, change_map):
  num_digits = 2 #len(str(len(x)))
  expected = bin(int(x, 2) + int(y, 2))[2:]
  #print(bin(int(x, 2) + int(y, 2))[2:], int(x, 2), int(y, 2))
  registers = {}
  for i, bit in enumerate(x[::-1]):
    registers[f'x{str(i).zfill(num_digits)}'] = int(bit)
  for i, bit in enumerate(y[::-1]):
    registers[f'y{str(i).zfill(num_digits)}'] = int(bit)

  for gate in gates:
    eval(registers, gates, gate)
  result = ''
  for i in range(len(x)+1):
    result = str(registers[f'z{str(i).zfill(num_digits)}']) + result
  diffs = set()
  for i in range(len(expected)):
    if result[-i-1] != expected[-i-1]:
      diffs.add(f'z{str(i).zfill(num_digits)}')    
  for diff in diffs:
    if diff not in change_map:
      change_map[diff] = 0
    change_map[diff] += 1
    for dependency in dependencies[diff]:
      if dependency not in change_map:
        change_map[dependency] = 0
      change_map[dependency] += 1

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  registers = {}
  gates = {}
  dependencies = {}
  found = False
  for line in file.readlines():    
    if line == "\n":
      found = True
      continue
    if found:
      parts = line.strip().split(" ")
      g1, gate, g2, g3 = parts[0], parts[1], parts[2], parts[4]
      gates[g3] = (g1, gate, g2)    
      dependencies[g3] = {g1, g2}
    else:
      gate, value = line.strip().split(": ")
      registers[gate] = int(value)
  """
  get_full_dependencies(dependencies)
  change_map = {}
  for i in range(100000):
    if i % 1000 == 0:
      print(i)
    test_x = bin(random.randint(0, 2**45-1))[2:].zfill(45)
    test_y = bin(random.randint(0, 2**45-1))[2:].zfill(45)
    simulate(test_x, test_y, gates, dependencies, change_map)
  """
  
  #part1(registers, gates)
  dot = get_dot(gates)
  with open('./graph.dot', 'w') as file:
    file.write(dot)    
  

if __name__ == "__main__":
  main(sys.argv[1:])
