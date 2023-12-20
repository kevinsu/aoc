import sys
import re
import common.io as io

class Segment():
  def __init__(self, x1, y1, x2, y2, color=None):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.color = color

  def __str__(self):
    return '(%d, %d)->(%d, %d): %s' % (self.x1, self.y1, self.x2, self.y2, self.color)

def get_shoelace(segments):
  count = 0
  for segment in segments:
    matrix = segment.x2 * segment.y1 - segment.x1 * segment.y2
    length = abs(segment.x2 - segment.x1 + segment.y2 - segment.y1)
    count += matrix + length 
  print(count/2 + 1)

def get_instructions(input):
  instructions = []
  file = open(input, 'r')
  for line in file.readlines():
    match = re.match('^\w\s\d+\s\(#(.*)(\d)\)', line)  
    direction = match.group(2)
    length = int(match.group(1), 16) 
    instructions.append((direction, length))
  return instructions

def get_segments(instructions):
  x1 = 0
  y1 = 0
  x2 = 0
  y2 = 0
  segments = []
  for direction, length in instructions:
    if direction == '0':
      y2 = y1 + length
    elif direction == '2':
      y2 = y1 - length
    elif direction == '1':
      x2 = x1 + length
    elif direction == '3':
      x2 = x1 - length
    segments.append(Segment(x1, y1, x2, y2)) 
    x1 = x2
    y1 = y2
  return segments 
     
def main(argv):
  instructions = get_instructions(argv[0])
  segments = get_segments(instructions)
  get_shoelace(segments)

if __name__ == "__main__":
  main(sys.argv[1:])
