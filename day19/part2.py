import sys
import inspect
import re
import copy

class Expression():
  def __init__(self, category, operation, value):
    self.category = category
    self.operation = operation
    self.value = int(value)
  
  def __str__(self):
    if self.value == 'A' or self.value == 'R':
      return self.value
    if not self.operation:
      return self.value
    return '%s%s%s' % (self.category, self.operation, self.value)

  def get_inverse(self):
    if self.operation == '<':
      return Expression(self.category, '>', self.value-1) 
    else:
      return Expression(self.category, '<', self.value+1)

class Workflow():
  def __init__(self, input_string):
    self.name = None 
    self.requirements = []
    self.input_string = input_string
    self.parse_input(input_string)

  def parse_input(self, input_string):
    match = re.match('(\w+)\{(.*)\}$', input_string)
    self.name = match.group(1)
    for input in match.group(2).split(','):
      req = input if ':' not in input else input.split(':')[1]
      if req != 'A' and req != 'R':
        self.requirements.append(req)

  def get_expressions(self, completed):
    match = re.match('(\w+)\{(.*)\}$', self.input_string)   
    name = match.group(1)  
    results = []
    next = []
    for input in match.group(2).split(','):
      expressions = next.copy() 
      if input == 'A' or input == 'R':
        expressions.append(input)
        results.append(expressions)
        break
      if ':' not in input:
        for r in completed[input]: 
          results.append(expressions + r)
        break
      match = re.match('^(\w+)(.)(\d+)\:(\w+)$', input)
      category = match.group(1)
      operation = match.group(2)
      value = int(match.group(3))
      result = match.group(4)
      expression = Expression(category, operation, value) 
      expressions.append(str(expression))
      inverse = expression.get_inverse() 
      next.append(str(inverse))
      if result == 'A' or result == 'R':
        expressions.append(result)
        results.append(expressions)
      else:
        for r in completed[result]:
          results.append(expressions + r)
    return results

def count(results):
  sum = 0
  for result in results:
    if result[-1] == 'R':
      continue
    count = {'x' : 4000, 'm' : 4000, 'a' : 4000, 's': 4000}
    accepted = {'x' : {}, 'm' : {}, 'a' : {}, 's': {}}
    for input in result[0:-1]:
      match = re.match('^(\w)(.)(\d+)$', input)
      expression = Expression(match.group(1), match.group(2), match.group(3))        
      if expression.operation == '<':
        for i in range(expression.value, 4001):
          if i in accepted[expression.category]:
            continue
          accepted[expression.category][i] = False 
          count[expression.category] -= 1
      else:
        for i in range(0, expression.value):
          if i in accepted[expression.category]:
            continue
          accepted[expression.category][i] = False
          count[expression.category] -= 1
    sum += count['x'] * count['m'] * count['a'] * count['s'] 
  print(sum)

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  workflows = {}
  completed = {}
  parts = []
  saw_newline = False
  not_done = {} 
  for line in file.readlines():
    if line == "\n":
      saw_newline = True
      continue
    if saw_newline:
      break
    workflow = Workflow(line.strip())
    workflows[workflow.name] = workflow
    if not workflow.requirements:
      completed[workflow.name] = workflow.get_expressions(completed)
    else:
      not_done[workflow.name] = workflow
  while not_done:
    to_pop = []
    for name, workflow in not_done.items():
      ready = all(req in completed for req in workflow.requirements)
      if ready:
        completed[name] = workflow.get_expressions(completed)
        to_pop.append(name)
    for name in to_pop:
      del not_done[name]
  count(completed['in'])

if __name__ == "__main__":
  main(sys.argv[1:])
