import re

class Node():
  def __init__(self, input_string):
    m = re.search("^(\w{3}).*\((\w{3}).*(\w{3})\)", input_string)
    self.name = m.group(1) 
    self.left = m.group(2)
    self.right = m.group(3)

  def get(self, left_or_right):
    if left_or_right == 'L':
      return self.left
    return self.right
