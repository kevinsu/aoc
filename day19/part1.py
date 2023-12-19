import sys
import re

class Workflow():
  def __init__(self, input_string):
    self.name = None 
    self.lambdas = []
    self.parse_input(input_string)

  def parse_input(self, input_string):
    match = re.match('(\w+)\{(.*)\}$', input_string)
    self.name = match.group(1)
    self.lambdas = [self.build_lambda(input) for input in match.group(2).split(',')]

  def build_lambda(self, input):
    if ':' not in input: 
      return (lambda part: True, input) 
    match = re.match('^(\w+)(.)(\d+)\:(\w+)$', input) 
    category = match.group(1)
    expression = match.group(2)
    value = int(match.group(3))
    result = match.group(4)
    if expression == '<':
      return (lambda part: part[category] < value, result)
    else:
      return (lambda part: part[category] > value, result)

  def process(self, part):
    for f, result in self.lambdas:
      if f(part):
        return result
    raise Exception('No valid lambda')

def build_part(input):
    match = re.match('\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', input)
    return {'x' : int(match.group(1)), 'm' : int(match.group(2)), 'a' : int(match.group(3)), 's' : int(match.group(4))}

def process(workflows, parts):
  sum = 0
  for part in parts:
    result = 'in'
    while(result != 'A' and result != 'R'):
      workflow = workflows[result]
      result = workflow.process(part)
    if result == 'A':
      sum += part['x'] + part['m'] + part['a'] + part['s']
    print(part, result) 
  print(sum)

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  workflows = {}
  parts = []
  saw_newline = False
  for line in file.readlines():
    if line == "\n":
      saw_newline = True
      continue
    if saw_newline:
      parts.append(build_part(line.strip())) 
    else:
      workflow = Workflow(line.strip())
      workflows[workflow.name] = workflow
  process(workflows, parts)
    

if __name__ == "__main__":
  main(sys.argv[1:])
