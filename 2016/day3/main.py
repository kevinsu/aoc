import sys
from common.perf import profiler

def is_triangle(s1, s2, s3):
  return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  count1 = 0
  count2 = 0
  t1 = []
  t2 = []
  t3 = []
  for i, line in enumerate(file.readlines()):
    splits = line.split()
    t1.append(int(splits[0]))
    t2.append(int(splits[1]))
    t3.append(int(splits[2]))
    if i%3==2:
      count2 += 1 if is_triangle(*t1) else 0
      count2 += 1 if is_triangle(*t2) else 0
      count2 += 1 if is_triangle(*t3) else 0
      t1.clear()
      t2.clear()
      t3.clear()
    if is_triangle(int(splits[0]), int(splits[1]), int(splits[2])): 
      count1 += 1
  print('part 1: ', count1)
  print('part 2: ', count2)

if __name__ == "__main__":
  main(sys.argv[1:])
