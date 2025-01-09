import re
import sys
from common.perf import profiler
import itertools
from collections import defaultdict

class Valve:
  def __init__(self, name, rate, children):
    self.name = name
    self.rate = rate
    self.children = children
  
  def __str__(self):
    return f'Name: {self.name} Rate: {self.rate} Children: {self.children}'

def get_key(opened):
  return ",".join(sorted(map(lambda x: x[0], opened)))

def get_pressure(valves, order, limit):
  expected = 0
  for i, j, _ in order:
    expected += (limit - int(j)) * valves[i].rate
  return expected

def get_key_and_pressure(valves, order):
  names = []
  relief = 0
  for name, time_remaining in order:
    valve = valves[name]
    names.append(name)
    relief += (time_remaining - 1) * valve.rate
  return ",".join(sorted(names)), relief

def build_valve_mapping(valves, graph, limit):
  mapping = defaultdict(int)
  test = []
  queue = [(limit, 'AA', set(), [])]
  while queue:
    time_remaining, name, opened, order = queue.pop()
    key, pressure = get_key_and_pressure(valves, order)
    mapping[key] = max(mapping[key], pressure)    
    test.append(order)
    for neighbor, dt in graph[name].items():
      if neighbor in opened or neighbor == 'AA':
        continue
      if dt + 1 < time_remaining:
        queue.append((time_remaining-dt-1, neighbor, opened | {neighbor}, order + [(neighbor, time_remaining-dt)]))
  return mapping

def part1(valves, graph):
  mapping = build_valve_mapping(valves, graph, 30)
  return max(mapping.values())

def part2(valves, graph):
  mapping = build_valve_mapping(valves, graph, 26)
  relief = 0
  for me, elephant in itertools.combinations(mapping.keys(), 2):
    me_opened = set(me.split(","))
    elephant_opened = set(elephant.split(","))
    if me_opened.isdisjoint(elephant_opened):
      new_relief = mapping[me] + mapping[elephant]
      relief = max(relief, new_relief)
  return relief
  
def floyd_warshall(valves):
  dist = {}
  for valve in valves.values():
    dist[valve.name] = defaultdict(lambda: sys.maxsize)
    for child in valve.children:
      dist[valve.name][child] = 1
  for k in valves:
    for i in valves:
      for j in valves:
        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
  return dist
  
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  valves = {}
  max_rate = 0
  active = {'AA'}
  for line in file.readlines():
    m = re.match("Valve (\w*) has flow rate=(\d+); tunnel(s?) lead(s?) to valve(s?) ([\s\S]*)", line)
    name, rate, _, _, _, children = m.groups()
    valve = Valve(name, int(rate), list(map(lambda x: x.strip(), children.strip().split(","))))
    valves[name] = valve
    max_rate += valve.rate
    if valve.rate > 0:
      active.add(name)
  dist = floyd_warshall(valves)
  graph = defaultdict(dict)
  for v1, v2 in itertools.combinations(active, 2):
    graph[v1][v2] = dist[v1][v2]
    graph[v2][v1] = dist[v2][v1]
  print(part1(valves, graph))
  print(part2(valves, graph))
  
if __name__ == "__main__":
  main(sys.argv[1:])
