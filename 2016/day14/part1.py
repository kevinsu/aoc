import sys
from common.perf import profiler
import hashlib

@profiler
def main(argv):
  input = 'zpqevtbw'
  print(get_index(input))
  
def get_hex_digest_2(input, index):
  string_to_hash = f"{input}{index}"
  hash_object = hashlib.md5(string_to_hash.encode())
  return hash_object.hexdigest()

def get_hex_digest(input, index):
  string_to_hash = f"{input}{index}"
  for i in range(0, 2017):
    hash_object = hashlib.md5(string_to_hash.encode())
    string_to_hash = hash_object.hexdigest()
  return string_to_hash

def get_earliest_triple(hex_digest):
  current_index = 100
  current_c = None
  for c in '0123456789abcdef':
    index = hex_digest.find(c*3)
    if index == -1:
      continue
    if index < current_index:
      current_c = c
  return current_c

  
def get_index(input):
  pads = []
  triples = {}  
  for c in '0123456789abcdef':
    triples[c] = []
  index = 0
  while len(pads) < 64:
    hex_digest = get_hex_digest(input, index)
    for c in '0123456789abcdef':
      if c*5 in hex_digest:       
        candidates = triples[c]
        for candidate in candidates:
          if candidate > index - 1000:
            pads.append(candidate)               
        triples[c] = [index]    
    earliest_triple = get_earliest_triple(hex_digest)
    if earliest_triple:
      triples[earliest_triple].append(index)
    index+=1
    
  for i in range(index, index+1000):
    hex_digest = get_hex_digest(input, i)
    for c in '0123456789abcdef':
      if c*5 in hex_digest:
        candidates = triples[c]
        for candidate in candidates:
          if candidate > index - 1000:
            pads.append(candidate)
        triples[c] = []
  pads.sort()
  print(pads)
  return pads[63]  


if __name__ == "__main__":
  main(sys.argv[1:])
