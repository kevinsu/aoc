import sys
from common.perf import profiler

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  for line in file.readlines():
    print(line)

if __name__ == "__main__":
  main(sys.argv[1:])
