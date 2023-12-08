import sys
import math
from node import Node
from itertools import cycle

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  instructions = file.readline().strip()
  nodes = {}
  starting_nodes = []
  for line in file.readlines()[1:]:
    node = Node(line)
    if node.name.endswith('A'):
      starting_nodes.append(node.name)
    nodes[node.name] = node 
  current_node = 'AAA'
  steps_list = []
  for starting_node in starting_nodes:
    steps = 0
    current_node = starting_node
    for i in cycle(instructions):
      if current_node.endswith('Z'):
        break
      current_node = nodes[current_node].get(i)
      steps += 1
    steps_list.append(steps)
  print(math.lcm(*steps_list))
    
if __name__ == "__main__":
  main(sys.argv[1:])
