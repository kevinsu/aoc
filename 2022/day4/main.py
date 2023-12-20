import sys

def full_overlap(elf1, elf2):
  if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
    return True
  return elf2[0] <= elf1[0] and elf2[1] >= elf1[1]

def partial_overlap(elf1, elf2):
  return not(elf1[1] < elf2[0] or elf1[0] > elf2[1])

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  part1 = 0
  part2 = 0
  for line in file.readlines():
    elves = line.strip().split(',')
    elf1 = tuple(map(int, elves[0].split('-')))
    elf2 = tuple(map(int, elves[1].split('-')))
    if full_overlap(elf1, elf2):
      part1 += 1
    if partial_overlap(elf1, elf2):
      part2 += 1 
  print(part1)
  print(part2)

if __name__ == "__main__":
  main(sys.argv[1:])
