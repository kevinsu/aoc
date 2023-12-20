import sys
import re

def get_num_winning(line):
  card, numbers = line.split(':')
  m = re.search("Card\s+(\d+)", card)
  card_id = m.group(1) 

  winning_numbers, player_numbers = numbers.split('|')
  winning_number_map = {}
  for number in winning_numbers.strip().split(' '):
    try:
      int(number)
      winning_number_map[number] = True  
    except:
      continue
  num_winning = 0
  for number in player_numbers.strip().split(' '):
    if number in winning_number_map:
      num_winning += 1
  return int(card_id), num_winning

def get_num_winning_map(input_file):
  file = open(input_file, 'r')
  num_winning_map = {}
  for line in file.readlines():
    card_id, num_winning = get_num_winning(line)
    num_winning_map[card_id] = num_winning
  return num_winning_map
  
def get_total_scratch_cards(num_winning_map):
  count = 0
  scratch_card_map = {}
  for card_id in num_winning_map.keys():
    scratch_card_map[card_id] = 1 
  for card_id in scratch_card_map.keys():
    num_winning = num_winning_map[card_id]
    for i in range(0, num_winning):
      scratch_card_map[card_id+i+1] += scratch_card_map[card_id] 
  return sum(scratch_card_map.values())

def main(argv):
  input_file = argv[0]
  num_winning_map = get_num_winning_map(input_file)
  print(get_total_scratch_cards(num_winning_map))

if __name__ == "__main__":
  main(sys.argv[1:])
