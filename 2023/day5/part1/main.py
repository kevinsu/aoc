import sys

from almanac import Almanac

def main(argv):
  input_file = argv[0]
  almanac = Almanac(input_file)
  seed_values = almanac.get_seed_values()
  print(min(seed_values))

if __name__ == "__main__":
  main(sys.argv[1:])
