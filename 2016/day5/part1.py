import sys
from hashlib import md5
from common.perf import profiler

@profiler
def main(argv):
  input = argv[0]
  count1 = 0
  count2 = 0
  i = 0
  code = ''
  part2 = ['_']*8
  while count1 < 8 or count2 < 8:
    s = f"{input}{i}" 
    key = md5(s.encode()).hexdigest()
    if key.startswith('00000'):
      if count1 < 8:
        count1 += 1
        code += key[5]
      try:
        index = int(key[5])
        if index < 8 and part2[index] == '_':
          part2[index] = key[6]
          count2 += 1
          print(''.join(part2))
      except:
        pass
    i+=1
  print('part 1: ', code)
  print('part 2: ', ''.join(part2))

if __name__ == "__main__":
  main(sys.argv[1:])
