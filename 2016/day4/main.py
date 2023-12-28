import sys
import re
from collections import defaultdict
from common.perf import profiler

LOOKUP = {
  'a' : 0,
  'b' : 1,
  'c' : 2,
  'd' : 3,
  'e' : 4,
  'f' : 5,
  'g' : 6,
  'h' : 7,
  'i' : 8,
  'j' : 9,
  'k' : 10,
  'l' : 11,
  'm' : 12,
  'n' : 13,
  'o' : 14,
  'p' : 15,
  'q' : 16,
  'r' : 17,
  's' : 18,
  't' : 19,
  'u' : 20,
  'v' : 21, 
  'w' : 22,
  'x' : 23, 
  'y' : 24,
  'z' : 25,
  0 : 'a',
  1 : 'b',
  2 : 'c',
  3 : 'd',
  4: 'e',
  5 : 'f',
  6 : 'g',
  7 : 'h',
  8 : 'i',
  9 : 'j',
  10 : 'k',
  11 : 'l',
  12 : 'm',
  13 : 'n',
  14 : 'o',
  15 : 'p',
  16: 'q',
  17 : 'r',
  18 : 's',
  19 : 't',
  20: 'u',
  21 : 'v',
  22 : 'w',
  23 : 'x',
  24 : 'y',
  25 : 'z',
}

def shift(name, sector):
  result = ''
  for c in name:
    if c == '-':
      result += ' '
      continue
    result += LOOKUP[(LOOKUP[c] + sector) % 26]
  return result

def is_real(line):
  match = re.match('^(.*)-(\d+)\[(.*)\]$', line.strip())
  name, sector, checksum = match.group(1, 2, 3)
  char_count = defaultdict(int) 
  for c in name:
    if c == '-':
      continue
    char_count[c] += 1
  if ''.join(sorted(map(lambda x: x[0], sorted(char_count.items(), key=lambda x: (-x[1], x[0]))[:5]))) == ''.join(sorted(checksum)):
    return int(sector), shift(name, int(sector)) 
  return 0, 'fake' 

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  part2 = 0
  for line in file.readlines():
    sector, name = is_real(line)
    if name == 'northpole object storage':
      part2 = sector
    sum += sector 
  print('part 1: ', sum)
  print('part 2: ', part2)

if __name__ == "__main__":
  main(sys.argv[1:])
