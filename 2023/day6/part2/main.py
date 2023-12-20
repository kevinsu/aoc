import sys
import math

def calculate_roots(b, c):
 return (b + math.sqrt(b*b - 4*c))/2, (b - math.sqrt(b*b - 4*c)) / 2 

def count_winners(x1, x2):
  new_x1 = math.floor(x1)
  new_x2 = math.ceil(x2)
  if new_x1 == x1:
    new_x1-=1
  if new_x2 == x2:
    new_x2+=1
  return new_x1 - new_x2 + 1 

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  time_input = file.readline()
  distance_input = file.readline()

  time = "".join(time_input.split()[1:])
  distance = "".join(distance_input.split()[1:])

  x1, x2 = calculate_roots(int(time), int(distance))
  print(count_winners(x1, x2))
  
  
if __name__ == "__main__":
  main(sys.argv[1:])
