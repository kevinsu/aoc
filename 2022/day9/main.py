import sys

def get_tail(hx, hy, tx, ty):
  # Touching
  if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
    return tx, ty
  if hx > tx:
    if hy > ty:
      return tx+1, ty+1
    elif hy < ty:
      return tx+1, ty-1
    return tx+1, ty
  elif hx < tx:
    if hy > ty:
      return tx-1, ty+1
    elif hy < ty:
      return tx-1, ty-1
    return tx-1, ty
  else:
    if hy > ty:
      return tx, ty+1
    elif hy < ty:
      return tx, ty-1
    return tx, ty 
  
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  hx = 0
  hy = 0
  tails = [(0, 0)]*9
  t_set = {(0, 0)}
  t_set2 = {(0, 0)}
  for line in file.readlines():
    direction, steps = line.split()
    for i in range(0, int(steps)):
      if direction == 'R':
        hx += 1
      elif direction == 'U':
        hy += 1
      elif direction == 'L':
        hx -= 1
      elif direction == 'D':
        hy -= 1
      temp_hx = hx
      temp_hy = hy
      for i, (tx, ty) in enumerate(tails):
        temp_hx, temp_hy = get_tail(temp_hx, temp_hy, tx, ty) 
        tails[i] = (temp_hx, temp_hy)
      t_set.add(tails[0])
      t_set2.add(tails[8])
  print(len(t_set))      
  print(len(t_set2))

if __name__ == "__main__":
  main(sys.argv[1:])
