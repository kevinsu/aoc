import sys
from common.perf import profiler

def compare_sls(s1, s2):
  for aba in s1:
    bab = aba[1] + aba[0] + aba[1]
    if bab in s2:
      return True
  return False

def supports(line):
  open_count = 0
  supports_tls = False
  tls_blacklist = False
  inside_aba = set()
  outside_aba = set()
  for i in range(0, len(line)-2):
    if line[i] == '[':
      open_count += 1
    if line[i] == ']':
      open_count -= 1
    is_abba = line[i:i+2] == line[i+2:i+4][::-1] and line[i] != line[i+1]
    is_aba = line[i] == line[i+2] and line[i] != line[i+1] and line[i+1] != '[' and line[i+1] != ']'
    if open_count > 0 and is_abba:
      tls_blacklist = True
    if is_aba:
      if open_count > 0:
        inside_aba.add(line[i:i+3])
      else:
        outside_aba.add(line[i:i+3])
    supports_tls = supports_tls or is_abba
  return supports_tls and not tls_blacklist, compare_sls(inside_aba, outside_aba)
    

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  part1 = 0
  part2 = 0
  for line in file.readlines():
    tls, sls = supports(line)
    if tls: 
      part1 += 1
    if sls:
      part2 += 1
  print('part 1: ', part1)
  print('part 2: ', part2)

if __name__ == "__main__":
  main(sys.argv[1:])
