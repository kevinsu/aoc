import re

from range import Range

class SeedMap():
  def __init__(self, input): 
    self.source = None
    self.destination = None
    self.ranges = []
    self.build_seed_map(input)
  
  def get_destination_intervals(self, start, range_length):
    covered_to_destination = {}
    for range in self.ranges:
      covered, destination = range.get_overlap(start, range_length)
      if not covered:
        continue
      covered_to_destination[covered] = destination
    begin = start
    intervals = []
    for interval in sorted(covered_to_destination.keys()):
      if begin < interval[0]:
        intervals.append((begin, interval[0]-1))    
      intervals.append(covered_to_destination[interval])
      begin = interval[0] + interval[1]
    if begin < start + range_length:
      intervals.append((begin, start + range_length - begin)) 
    return intervals

  def build_seed_map(self, input):
    m = re.search('^(\w+)\-.*\-(\w+)\smap', input[0])  
    self.source = m.group(1)
    self.destination = m.group(2)
    for line in input[1:]:
      destination, source, range = line.strip().split()
      self.ranges.append(Range(int(destination), int(source), int(range))) 
