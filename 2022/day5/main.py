import sys
import re

def parse_input(input_file):
  file = open(input_file, 'r')
  buckets = {}
  buckets2 = {}
  start_instructions = False
  for line in file.readlines():
    if line == '\n':
      start_instructions = True
      continue
    if '[' in line and not start_instructions:
      for i, crate in enumerate(line[1::4]):
        if not crate.strip():
          continue
        if i+1 not in buckets:
          buckets[i+1] = []
          buckets2[i+1] = []
        buckets[i+1].insert(0, crate)
        buckets2[i+1].insert(0, crate)
      continue
    if start_instructions:
      match = re.match('^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$', line.strip()) 
      print(match.group(1), match.group(2), match.group(3))
      num = int(match.group(1))
      start = int(match.group(2))
      to = int(match.group(3))
      buckets[to].extend(reversed(buckets[start][-num:]))
      buckets2[to].extend(buckets2[start][-num:])
      del buckets[start][-num:]
      del buckets2[start][-num:]
  result = ''
  result2 = ''
  for i in range(1, len(buckets)+1):
    result += buckets[i][-1]
    result2 += buckets2[i][-1]
  print(result)
  print(result2)
    

def main(argv):
  parse_input(argv[0])

if __name__ == "__main__":
  main(sys.argv[1:])
