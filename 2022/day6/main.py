import sys

def find_start(input, length):
  for i in range(0, len(input)):
    dupe = False
    seen = {}
    for c in input[i:i+length]:
      if c in seen:
        dupe = True
        break
      seen[c] = True
    if not dupe:
      break
  print(i+length)
    
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  line = file.readline().strip()
  find_start(line, 4)
  find_start(line, 14)
  

if __name__ == "__main__":
  main(sys.argv[1:])
