import sys

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  load = 0
  max_load = 0
  load_to_elf = {}
  elf = 1
  for line in file.readlines():
    if line == '\n':
      load_to_elf[load] = elf
      max_load = max(load, max_load)
      load = 0
      elf += 1 
      continue
    load += int(line.strip())
  print(max_load)
  print(sum(sorted(load_to_elf.keys())[-3:]))
    
if __name__ == "__main__":
  main(sys.argv[1:])
