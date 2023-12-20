from seed_map import SeedMap

class Almanac():
  def __init__(self, input_file):
    self.seeds = []
    self.seed_maps = {}
    self.parse_input(input_file)

  def parse_input(self, input_file):
    with open(input_file, 'r') as file:
      self.seeds = self.get_seed_intervals_from_line(file.readline())
      current_map = []      
      for line in file:
        if line == '\n':
          if current_map:
            seed_map = SeedMap(current_map)
            self.seed_maps[seed_map.source] = seed_map
          current_map = [] 
          continue
        current_map.append(line)
      if current_map:
        seed_map = SeedMap(current_map)
        self.seed_maps[seed_map.source] = seed_map
  
  def get_intervals(self):
    source = 'seed'
    intervals = self.seeds 
    while source != 'location':
      seed_map = self.seed_maps[source]
      temp = []
      for seed_interval in intervals: 
        temp.extend(seed_map.get_destination_intervals(seed_interval[0], seed_interval[1]))
      intervals = temp
      source = seed_map.destination
    return intervals 
  
  def get_seed_intervals_from_line(self, line):
    raw_seeds = iter(line.strip().split(':')[1].strip().split(' '))
    for start in raw_seeds:
      range_length = next(raw_seeds)
      yield(int(start), int(range_length)) 
