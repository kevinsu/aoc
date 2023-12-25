import sys
from collections import defaultdict
from copy import copy, deepcopy
from common.perf import profiler
import random

def build_graph(input):
  file = open(input, 'r')
  graph = defaultdict(set) 
  for line in file.readlines():
    node, neighbors = line.split(":")
    for neighbor in neighbors.split():
      graph[node].add(neighbor)
      graph[neighbor].add(node)
  return graph      

def build_graphviz(graph, output):
  file = open(output, 'w')
  file.write("digraph G {\n")
  for node, neighbors in graph.items():
    for neighbor in neighbors:
      file.write(f"  {node} -> {neighbor};\n")    
  file.write("}")
      
def main(argv):
  graph = build_graph(argv[0])
  counter = 0
  build_graphviz(graph, argv[1]) 

if __name__ == "__main__":
  main(sys.argv[1:])
