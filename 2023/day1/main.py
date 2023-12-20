import sys

NUMBERS = {
  'one' : 'o1e',
  'two' : 't2o',
  'three' : 't3e',
  'four' : 'f4r',
  'five' : 'f5e',
  'six' : 's6x',
  'seven' : 's7n',
  'eight' : 'e8t',
  'nine' : 'n9e',
}

def _get_calibration_value(line):
  for key, value in NUMBERS.items():
    line = line.replace(key, value)
  front = None
  for c in line:
    try:
      front = int(c)
      break
    except:
      continue
  back = None 
  for c in reversed(line):
    try:
      back = int(c)
      break
    except:
      continue
  if not front:
    return 0
  return int('%s%s' % (front, back))
    
      

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  sum = 0
  for line in file.readlines():
    sum += _get_calibration_value(line)
  print(sum)

if __name__ == "__main__":
  main(sys.argv[1:])
