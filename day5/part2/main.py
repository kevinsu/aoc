import sys

from almanac import Almanac

def main(argv):
  input_file = argv[0]
  almanac = Almanac(input_file)
  intervals = almanac.get_intervals()
  print(min(map(lambda x: x[0], intervals))) 

if __name__ == "__main__":
  main(sys.argv[1:])
