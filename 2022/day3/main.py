import sys

priorities = {
  'a' : 1,
  'b' : 2,
  'c' : 3,
  'd' : 4,
  'e' : 5,
  'f' : 6,
  'g' : 7,
  'h' : 8,
  'i' : 9,
  'j' : 10,
  'k' : 11,
  'l' : 12,
  'm' : 13,
  'n' : 14,
  'o' : 15,
  'p' : 16,
  'q' : 17,
  'r' : 18,
  's' : 19,
  't' : 20,
  'u' : 21,
  'v' : 22,
  'w' : 23,
  'x' : 24,
  'y' : 25,
  'z' : 26,
  'A' : 27,
  'B' : 28,
  'C' : 29,
  'D' : 30,
  'E' : 31,
  'F' : 32,
  'G' : 33,
  'H' : 34,
  'I' : 35,
  'J' : 36,
  'K' : 37,
  'L' : 38,
  'M' : 39,
  'N' : 40,
  'O' : 41,
  'P' : 42,
  'Q' : 43,
  'R' : 44,
  'S' : 45,
  'T' : 46,
  'U' : 47,
  'V' : 48,
  'W' : 49,
  'X' : 50,
  'Y' : 51,
  'Z' : 52,
}

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  part1 = 0
  part2 = 0
  group = [] 
  for i, line in enumerate(file.readlines()):
    group.append(line)
    if i % 3 == 2:
      sack1 = {}
      for c in group[0]:
        sack1[c] = True
      sack2 = {}
      for c in group[1]:
        sack2[c] = True
      for c in group[2]:
        if c in sack1 and c in sack2:
          part2 += priorities[c]
          break
      group = [] 
    length = int(len(line.strip())/2)
    r = {}
    for c in line[0:length]:
      r[c] = True
    for c in line[length:]:
      if c in r:
        part1 += priorities[c]
        break
  print("Part 1: ", part1)
  print("Part 2: ", part2)

if __name__ == "__main__":
  main(sys.argv[1:])
