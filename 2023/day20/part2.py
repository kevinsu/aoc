import sys
import math
import re

class Executor():
  def __init__(self):
    self.cycle_count = 0
    self.commands = []
    self.modules = {}
    self.high_count = 0
    self.low_count = 0
    self.candidates = {} 
    self.done = False

  def track(self, candidates):
    for candidate in candidates:
      self.candidates[candidate] = 0

  def lcm(self):
    return math.lcm(*self.candidates.values())

  def count(self, sender, child, pulse):
    if pulse:
      self.high_count += 1
    else:
      self.low_count += 1
    if (sender, child) in self.candidates and pulse:
      if not self.candidates[(sender, child)]:
        self.candidates[(sender, child)] = self.cycle_count
      if all(self.candidates.values()):
        self.done = True

  def send(self, sender, children, pulse):
    for child in children:
      self.count(sender, child, pulse)
      self.commands.append((sender, self.modules[child], pulse)) 

  def execute(self):
    self.cycle_count += 1
    while self.commands:
      sender, module, pulse = self.commands.pop(0)
      module.receive(sender, pulse)

  def is_on(self):
    is_on = False 
    for module in self.modules.values():
      if module.is_on():
        is_on = True
        break
    return is_on

class FlipFlop():
  def __init__(self, executor, name, children):
    self.on = False
    self.name = name
    self.executor = executor
    self.children = children

  def receive(self, sender, pulse):
    if pulse:
      return
    if not pulse:
      if not self.on:
        self.on = True
        self.executor.send(self.name, self.children, True)
      else:
        self.on = False
        self.executor.send(self.name, self.children, False)
  
  def is_on(self):
    return self.on

class Conjuction():
  def __init__(self, executor, name, children):
    self.name = name
    self.executor = executor
    self.children = children
    self.inputs = []
    self.memory = {}

  def set_inputs(self, inputs):
    for input in inputs:
      self.memory[input] = False

  def receive(self, sender, pulse):
    self.memory[sender] = pulse 
    if all(self.memory.values()): 
      self.executor.send(self.name, self.children, False)
    else:
      self.executor.send(self.name, self.children, True)

  def is_on(self):
    return any(self.memory.values())

class Broadcast():
  def __init__(self, executor, name, children):
    self.executor = executor
    self.name = name
    self.children = children
  
  def receive(self, sender, pulse):
    self.executor.send(self.name, self.children, pulse)

  def is_on(self):
    return False

class Output():
  def __init__(self, name):
    self.name = name 

  def receive(self, sender, pulse):
    return  

  def is_on(self):
    return False

def get_tracking_candidates(output, parents):
  candidates = []
  parent = parents[output][0]
  for x in parents[parent]:
    candidates.append((x, parent)) 
  return candidates

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  executor = Executor()
  parents = {}
  conjuctions = []
  for line in file.readlines():
    match = re.match('^([%&]*)(.*)\s->\s(.*)$', line.strip())
    module_type = match.group(1) 
    name = match.group(2)
    children = [x.strip() for x in match.group(3).split(',')]
    if module_type == '%':
      executor.modules[name] = FlipFlop(executor, name, children)
    elif module_type == '&':
      executor.modules[name] = Conjuction(executor, name, children)
      conjuctions.append(name)
    else:
      executor.modules[name] = Broadcast(executor, name, children)
    for child in children:
      if child not in parents:
        parents[child] = []
      parents[child].append(name) 
  for conjuction in conjuctions:
    executor.modules[conjuction].set_inputs(parents[conjuction])
  child = None
  for child in parents.keys():
    if child not in executor.modules:
      output = child
  executor.modules[output] = Output(output) 
  candidates = get_tracking_candidates(output, parents)
  executor.track(candidates)
  
  button = Broadcast(executor, 'button', ['broadcaster'])

  while(True):
    if executor.done:
      break
    button.receive('button', False)
    executor.execute()
  print(executor.lcm())

if __name__ == "__main__":
  main(sys.argv[1:])
