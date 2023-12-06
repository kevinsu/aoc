import sys

LIMITS = {
  'red' : 12,
  'green' : 13,
  'blue' : 14
}

def get_power(rounds):
  mins = {
    'red': 0,
    'green': 0,
    'blue': 0
  }
  for round in rounds.split(';'):
    for draw in round.split(','):
      count, color = draw.strip().split(" ")
      if int(count) > mins[color]:
        mins[color] = int(count)
  return mins['red'] * mins['green'] * mins['blue']
      
def process_line(line):
  game_part, rounds = line.split(':')
  return get_power(rounds)

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    sum += process_line(line)
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
