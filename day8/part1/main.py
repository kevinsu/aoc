import sys
from node import Node
from itertools import cycle

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  instructions = file.readline().strip()
  nodes = {}
  for line in file.readlines()[1:]:
    node = Node(line)
    nodes[node.name] = node 
  current_node = 'AAA'
  steps = 0
  for i in cycle(instructions):
    if current_node == 'ZZZ':
      break
    current_node = nodes[current_node].get(i)
    steps += 1
  print(steps)
    
if __name__ == "__main__":
  main(sys.argv[1:])
