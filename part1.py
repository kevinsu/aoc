import sys

LIMITS = {
  'red' : 12,
  'green' : 13,
  'blue' : 14
}

def verify_rounds(rounds):
  for round in rounds.split(';'):
    for draw in round.split(","):
      count, color = draw.strip().split(" ")
      limit = LIMITS[color.strip()]
      count = int(count.strip())
      if count > limit:
        return False
  return True

def process_line(line):
  game_part, rounds = line.split(':')
  game_id = int(game_part.split(' ')[1])
  is_valid = verify_rounds(rounds) 
  return is_valid, game_id

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    is_valid, game_id = process_line(line)
    if is_valid:
      sum += game_id
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
