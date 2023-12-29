import sys
from common.perf import profiler

TARGET = [17, 61]

class Bot:
  def __init__(self, id):
    self.id = id
    self.values = []
    self.low = None
    self.high = None

  def __str__(self):
    return '%s low: %s high: %s' % (self.id, self.low.id if self.low else 'None', self.high.id if self.high else 'None')
  
  def add_low_high(self, low, high):
    self.low = low
    self.high = high

  def add_value(self, value):
    self.values.append(value)
    if sorted(self.values) == TARGET:
      print('part1: ', self.id) 
    if len(self.values) == 2:
      self.low.add_value(min(self.values))
      self.high.add_value(max(self.values))
      values = []

class Output:
  def __init__(self, id):
    self.id = id
    self.values = []

  def __str__(self):
    return '%s %s' % (self.id, self.values)

  def add_value(self, value):
    self.values.append(value)

def get_or_create_bot(bot_map, id, t):
  key = f"{t}-{id}"
  if key in bot_map:
    return bot_map[key]
  bot = None
  if t == "output":
    bot = Output(id)
  else:
    bot = Bot(id)
  bot_map[key] = bot
  return bot 
      
@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  bot_map = {}
  for line in sorted(file.readlines()):
    splits = line.split()
    if splits[0] == 'value':
      id = int(splits[5])
      bot = get_or_create_bot(bot_map, id, "bot")
      bot.add_value(int(splits[1]))
      continue
    # line starts with bot
    id1 = int(splits[1])
    bot1 = get_or_create_bot(bot_map, id1, "bot")
    
    id2 = int(splits[6])
    t2 = splits[5]
    bot2 = get_or_create_bot(bot_map, id2, t2)

    id3 = int(splits[11])
    t3 = splits[10]
    bot3 = get_or_create_bot(bot_map, id3, t3)

    bot1.low = bot2
    bot1.high = bot3
  print('part2: ', bot_map['output-0'].values[0] *bot_map['output-1'].values[0] * bot_map['output-2'].values[0])

if __name__ == "__main__":
  main(sys.argv[1:])
