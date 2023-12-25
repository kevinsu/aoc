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

def get_new_node(edge):
  return ':'.join(sorted(edge[0].split(':') + edge[1].split(':')))

def build_edges(graph):
  edges = set()
  for node, neighbors in graph.items():
    for neighbor in neighbors:
      edge = tuple(sorted([node, neighbor]) + [':'.join(sorted([node, neighbor]))])
      edges.add(edge)
  return edges

def pretty_print(graph):
  for key, value in sorted(graph.items()):
    print(key, value)

def ppe(edges):
  for value in sorted(edges, key=lambda x: x[2]):
    print(value)

@profiler
def contract_graph(graph, edges):
  while len(graph) > 2:
    edge = random.choice(list(edges))
    edges.remove(edge)
    new_node = get_new_node(edge) 
    # Update neighbors of a and b to point to a:b
    neighbors1 = graph[edge[0]] or set()
    neighbors2 = graph[edge[1]] or set()
    for neighbor in neighbors1:
      graph[neighbor] = graph[neighbor] - {edge[0]} 
      graph[neighbor].update({new_node})
    for neighbor in neighbors2:
      graph[neighbor] = graph[neighbor] - {edge[1]}
      graph[neighbor].update({new_node})
    # Move all neighbors of b into a, minus self loops
    graph[new_node] = neighbors1.union(neighbors2) - {edge[0]} - {edge[1]}
    del graph[edge[0]]
    del graph[edge[1]]
    new_edges = []
    # Update edges
    for e in edges:
      if edge[0] not in e and edge[1] not in e:
        new_edges.append(e)
        continue
      n1 = e[0] if e[0] not in edge else new_node
      n2 = e[1] if e[1] not in edge else new_node
      if n1 == n2:
        continue
      new_edges.append(tuple(sorted([n1, n2]) + [e[2]]))
    edges = new_edges
  return graph, edges
   
def main(argv):
  graph = build_graph(argv[0])
  edges = build_edges(graph)
  counter = 0
  while True:
    counter += 1
    if counter % 2 == 0:
      print(f"Tried {counter} times")
    g = deepcopy(graph)  
    e = deepcopy(edges)
    g, e = contract_graph(g, e)
    if len(e) == 3:
      product = 1
      for key in g:
        product *= len(key.split(':'))
      print(product)
      break

if __name__ == "__main__":
  main(sys.argv[1:])
