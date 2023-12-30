import sys
import itertools
import heapq
from common.perf import profiler
from copy import deepcopy
import re

def get_state_string2(state):
  result = ''
  for i in range(0, len(state[1])):
    result += str(i+1) + ','.join(sorted(state[1][i]))
  return '%s:%s' % (state[0], result)

def get_state_string(state):
  generators = {}
  microchips = {}
  for i in range(0, len(state[1])):
    floor = state[1][i] 
    for obj in floor:
      element, t = obj.split('-')
      if t == 'g':
        generators[element] = i
      else:
        microchips[element] = i
  pairs = []
  for key in microchips.keys():
    pairs.append((generators[key], microchips[key]))
  return '%s:%s' % (state[0], str(sorted(pairs)))
    
      
def get_distance(state):
  sum = 0
  for i in range(0, len(state[1])):
    sum += len(state[1][i]) * (3-i) 
  return sum

def is_finished(state):
  for i in range(0, len(state[1])-1):
    if len(state[1][i]) != 0:
      return False
  return True
  
# State = (Elevator floor, configuration)
def parse_input(input):
  file = open(input, 'r')
  configuration = []
  for line in file.readlines():
    floor = set()
    sentence = line.split('contains')
    if sentence[1].find('nothing') != -1:
      configuration.append(floor)
      continue
    for part in sentence[1].split(' a '):               
      if not part.strip():
        continue
      match = re.search('(\w+)((-compatible)?)\s', part)
      if match.group(2):
        floor.add("%s-m" % match.group(1))
      else:
        floor.add("%s-g" % match.group(1))
    configuration.append(floor) 
  return (0, configuration)

def is_floor_valid(elevator, floor):
  generators = set() 
  microchips = set()
  for obj in floor:
    element, t = obj.split('-')
    if t == 'g':
      generators.add(element)
    else:
      microchips.add(element)
  if len(generators) == 0:
    return True
  for m in microchips:
    if m not in generators:
      return False 
  return True

def get_next_states(state):
  elevator, configuration = state
  objs = configuration[elevator]
  possibilities = list(map(set, list(itertools.combinations(objs, 2)) + list(itertools.combinations(objs,1))))
  for possibility in possibilities:
    upstairs = elevator+1 < len(configuration) and is_floor_valid(elevator+1, configuration[elevator+1].union(possibility))
    current = is_floor_valid(elevator, configuration[elevator]-possibility)
    downstairs = elevator-1 >= 0 and is_floor_valid(elevator-1, configuration[elevator-1].union(possibility))
    if not current:
      continue
    if upstairs:
      config = deepcopy(configuration)
      config[elevator] = configuration[elevator]-possibility
      config[elevator+1].update(possibility)
      yield (elevator+1, config) 
    if downstairs:
      config = deepcopy(configuration)
      config[elevator] = configuration[elevator]-possibility
      config[elevator-1].update(possibility)
      yield (elevator-1, config) 
     
def find_shortest(state):
  visited = set() 
  #todo = [(0, state)]
  todo = []
  heapq.heappush(todo, (get_distance(state), 0, state))
  counter = 0
  visited_counter = 0
  while todo:
    counter += 1
    current_distance, num_steps, current_state = heapq.heappop(todo)
    #num_steps, current_state = todo.pop(0)
    if is_finished(current_state):
      print(counter)
      return num_steps
    current_key = get_state_string(current_state)
    if current_key in visited:
      visited_counter += 1 
      continue
    visited.add(current_key)
    for next_state in get_next_states(current_state):
      next_key = get_state_string(next_state)
      if next_key in visited:
        continue 
      heapq.heappush(todo, (get_distance(next_state)+num_steps+1, num_steps+1, next_state))
      #todo.append((num_steps+1, next_state))

@profiler
def main(argv):
  state = parse_input(argv[0]) 
  distance = find_shortest(state)
  print(distance)
    

if __name__ == "__main__":
  main(sys.argv[1:])
