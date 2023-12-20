import sys

def get_line_value(line):
  numbers = line.split(':')[1]
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
  value = 0
  if num_winning > 0:
    value = 2**(num_winning-1)
  return value

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    sum += get_line_value(line)
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
