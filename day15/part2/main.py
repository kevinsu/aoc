import sys
import re

class Box():
  def __init__(self, number):
    self.number = number
    self.labels = []
    self.label_to_length_map = {}
  
  def __str__(self):
    labels = ['Box %s:' % self.number]
    for label in self.labels:
      labels.append('[%s %d]' % (label, self.label_to_length_map[label]))
    return ' '.join(labels) 

  def update_box(self, label, operation, length):
    if operation == '-':
      if label in self.label_to_length_map:
        self.labels.remove(label)
        del self.label_to_length_map[label]
    else:
      if label not in self.label_to_length_map:
        self.labels.append(label)
      self.label_to_length_map[label] = int(length)

  def get_power(self):
    power = 0
    for i, label in enumerate(self.labels):
      power += (i+1) * self.label_to_length_map[label]
    return (self.number + 1) * power

def update_boxes(label, operation, length, boxes):
  box_number = hash(label)
  if box_number not in boxes:
    boxes[box_number] = Box(box_number)
  boxes[box_number].update_box(label, operation, length) 

def hash(step):
  current_value = 0
  for c in step:
    current_value += ord(c)
    current_value *= 17
    current_value %= 256
  return current_value

def print_boxes(boxes):
  for i in range(0, 10):
    if i not in boxes:
      continue
    print(boxes[i])

def parse_line(line):
  steps = line.strip().split(",")
  sum = 0
  boxes = {}
  for step in steps:
    match = re.match('^(\w+)([-=])(\d*)$', step) 
    label = match.group(1)
    operation = match.group(2)
    length = match.group(3)
    update_boxes(label, operation, length, boxes) 
  sum = 0
  for box in boxes.values():
    sum += box.get_power() 
  print(sum)


def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  parse_line(file.readline())

if __name__ == "__main__":
  main(sys.argv[1:])
