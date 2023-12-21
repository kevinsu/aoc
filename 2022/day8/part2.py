import sys
from common.io import get_2d_int_array_from_file as build_input
from common.io import pretty_print 

def check(input, i, j):
  left = 0
  right = 0
  up = 0
  down = 0
  offset = 1 
  while offset + j < len(input[0]): 
    right += 1
    if input[i][j] > input[i][j+offset]:
      offset += 1
    else:
      break
  offset = 1 
  while j-offset >= 0:
    left += 1
    if input[i][j] > input[i][j-offset]:
      offset += 1
    else:
      break
  offset = 1
  while i-offset >= 0:
    up += 1
    if input[i][j] > input[i-offset][j]:
      offset += 1
    else:
      break
  offset = 1
  while i+offset < len(input):
    down += 1
    if input[i][j] > input[i+offset][j]:
      offset += 1
    else:
      break
  return left, right, up, down

def count_visible(input):
  max_view = 0
  for i in range(0, len(input)):
    for j in range(0, len(input[0])):
      left, right, up, down = check(input, i, j)    
      view = left * right * up * down 
      max_view = max(max_view, view)
  print(max_view)
      

def main(argv):
  input = build_input(argv[0]) 
  count_visible(input)

if __name__ == "__main__":
  main(sys.argv[1:])
