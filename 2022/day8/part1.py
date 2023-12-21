import sys
from common.io import get_2d_int_array_from_file as build_input
from common.io import pretty_print 

def count_visible(input):
  visible = [[False]*len(input[0]) for row in input] 
  for i, row in enumerate(input):
    blocker = -1 
    for j, cell in enumerate(row):
      if blocker < cell:
        visible[i][j] = True
        blocker = cell
    blocker = -1 
    for j, cell in enumerate(reversed(row)):
      if blocker < cell:
        visible[i][len(row)-1-j] = True
        blocker = cell
  for j in range(0, len(input[0])):
    blocker = -1 
    for i in range(0, len(input)):
      cell = input[i][j]
      print(i, j, cell)
      if blocker < cell:
        visible[i][j] = True
        blocker = cell
    blocker = -1
    for i in range(0, len(input)):
      cell = input[len(input)-1-i][j]
      if blocker < cell:
        visible[len(input)-1-i][j] = True
        blocker = cell
  pretty_print(visible)
  print(sum([sum(row) for row in visible]))      
      

def main(argv):
  input = build_input(argv[0]) 
  pretty_print(input)
  count_visible(input)

if __name__ == "__main__":
  main(sys.argv[1:])
