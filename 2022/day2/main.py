import sys

wld = {
  'A': {'X' : 'Z', 'Y' : 'X', 'Z' : 'Y'},
  'B': {'X' : 'X', 'Y' : 'Y', 'Z' : 'Z'},
  'C': {'X' : 'Y', 'Y' : 'Z', 'Z' : 'X'},
}

result = {
  'A': {'X' : 4, 'Y' : 8, 'Z' : 3},
  'B': {'X' : 1, 'Y' : 5, 'Z' : 9},
  'C': {'X' : 7, 'Y' : 2, 'Z' : 6},
}

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    them, us = line.strip().split()
    sum += result[them][wld[them][us]]
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
