import re

from range import Range

class SeedMap():
  def __init__(self, input): 
    self.source = None
    self.destination = None
    self.ranges = []
    self.build_seed_map(input)
  
  def get_destination_number(self, source_number):
    for range in self.ranges:
      if range.contains(source_number):
        return range.get_destination_number(source_number)
    return source_number

  def build_seed_map(self, input):
    m = re.search('^(\w+)\-.*\-(\w+)\smap', input[0])  
    self.source = m.group(1)
    self.destination = m.group(2)
    for line in input[1:]:
      destination, source, range = line.strip().split()
      self.ranges.append(Range(int(destination), int(source), int(range))) 
