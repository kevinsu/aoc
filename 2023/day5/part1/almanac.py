from seed_map import SeedMap

class Almanac():
  def __init__(self, input_file):
    self.seeds = []
    self.seed_maps = {}
    self.parse_input(input_file)

  def parse_input(self, input_file):
    with open(input_file, 'r') as file:
      self.seeds = self.get_seeds_from_line(file.readline())
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
  
  def get_seed_values(self):
    for seed in self.seeds:
      source = 'seed'
      value = seed
      while source != 'location':
        seed_map = self.seed_maps[source]
        value = seed_map.get_destination_number(value) 
        source = seed_map.destination
      yield value
  
  def get_seeds_from_line(self, line):
    return map(int, line.strip().split(':')[1].strip().split(' ')) 
