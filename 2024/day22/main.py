from collections import defaultdict
from math import floor
import sys
from common.perf import profiler

def mix(given, secret):
  return given ^ secret

def prune(secret):
  return secret % 16777216

def get_next(secret):
  s1 = prune(mix(secret * 64, secret))
  s2 = prune(mix(floor(s1/32), s1))
  return prune(mix(s2*2048, s2))

def get_change_map(sequence):
  change_map = {}
  for i in range(0, len(sequence)-4):
    d1 = sequence[i+1]%10-sequence[i]%10
    d2 = sequence[i+2]%10-sequence[i+1]%10
    d3 = sequence[i+3]%10-sequence[i+2]%10
    d4 = sequence[i+4]%10-sequence[i+3]%10
    if (d1, d2, d3, d4) in change_map:
       continue
    change_map[(d1, d2, d3, d4)] = sequence[i+4]%10    
  return change_map

def get_sequence(secret, num_steps):
  next_secret = secret
  sequence = [secret]
  for _ in range(num_steps):
    next_secret = get_next(next_secret)    
    sequence.append(next_secret)
  change_map = get_change_map(sequence)
  return next_secret, change_map

def get_best_sequence(change_maps, sequences):
  best = 0  
  for sequence in sequences:      
      total = sum(change_map.get(sequence, 0) for change_map in change_maps)
      if total > best:
        best = total              
  return best

def part1(secrets, num_steps):
  sum = 0
  change_maps = []
  sequences = set()
  for secret in secrets:
    res, change_map = get_sequence(secret, num_steps)
    sum += res
    change_maps.append(change_map)
    sequences.update(change_map.keys())
  best_sequence = get_best_sequence(change_maps, sequences)
  return sum, best_sequence

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  secrets = []
  for line in file.readlines():
    secrets.append(int(line))
  print(part1(secrets, 2000))  

if __name__ == "__main__":
  main(sys.argv[1:])
