from math import floor

class CycleFinder:
  def __init__(self):
    self.start_key = None
    self.start_count = None
    self.start_value = None
    self.mapping = {}
    self.cycle_length = None
    self.cycle_value = None
    self.cycle_map = {}
  
  def find_cycle(self, key, count, value):
    if key == self.start_key:
      self.cycle_length = count - self.start_count
      self.cycle_value = value - self.start_value
      print("Cycle completed: ", count-self.start_count, value-self.start_value)
      return True
    if key in self.mapping:
      if not self.start_count:
        print("Cycle start: ", count, value)
        self.start_key = key
        self.start_count = count
        self.start_value = value 
      else:
        self.cycle_map[count-self.start_count] = value - self.start_value 
    self.mapping[key] = value
    return False

  def calculate_step(self, step):
    multiplier = floor((step - self.start_count) / self.cycle_length)
    remainder = step - self.start_count - multiplier * self.cycle_length
    return self.start_value + self.cycle_value * multiplier + self.cycle_map[remainder]
