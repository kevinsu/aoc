import itertools
import sys
from common.perf import profiler

NUM_PAD = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2)
}

DIR_PAD = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

def helper(sx, sy, ex, ey, is_num_pad=True):    
    if sx < 0:
        return set()
    if sy < 0:
        return set()
    if sx == ex and sy == ey:
        return set()
    if is_num_pad and (sx, sy) == (3, 0):
        return set()
    if not is_num_pad and (sx, sy) == (0, 0):
        return set()
    
    dx = sx - ex
    dy = sy - ey
    cx = '^'
    if dx < 0:
        cx = 'v'
    cy = '<'
    if dy < 0:
        cy = '>'
    if dx == 0:
        return [cy*abs(dy)]
    if dy == 0:
        return [cx*abs(dx)]    
    ddx = int(dx / abs(dx))
    ddy = int(dy / abs(dy))
    result = set()
    if ddx != 0:
        result = result | set(map(lambda x: cx + x, helper(sx-ddx, sy, ex, ey, is_num_pad=is_num_pad)))
    if ddy != 0:
        result = result | set(map(lambda x: cy + x, helper(sx, sy-ddy, ex, ey, is_num_pad=is_num_pad)))
    return result
                    

def translate(start, end, is_num_pad=True):
    possible = helper(start[0], start[1], end[0], end[1], is_num_pad=is_num_pad)
    return list(map(lambda x: x+'A', possible))

def part1(codes):
    sum = 0
    for code in codes:        
        sum += get_complexity(code, 2)
    return sum

def part2(codes):
    sum = 0
    for code in codes:        
        sum += get_complexity(code, 25)
    return sum

def calculate_cost_map(num_robots):
    lookup = {}
    for i, j in itertools.permutations(DIR_PAD.keys(), 2):
        shortest = sys.maxsize
        for p in translate(DIR_PAD[i], DIR_PAD[j], is_num_pad=False):
            if len(p) < shortest:
                shortest = len(p)
        lookup[(i, j)] = shortest
    
    for _ in range(1, num_robots):
      new_lookup = {}
      for i, j in itertools.permutations(DIR_PAD.keys(), 2):
          shortest = sys.maxsize
          for p in translate(DIR_PAD[i], DIR_PAD[j], is_num_pad=False):
              cost = 0
              for x, y in itertools.pairwise('A'+p):
                  cost += lookup.get((x, y), 1)
              if cost < shortest:
                  shortest = cost
          new_lookup[(i, j)] = shortest                
      lookup = new_lookup
    cost_map = {}
    for i, j in itertools.permutations(NUM_PAD.keys(), 2):
        shortest = sys.maxsize
        for p in translate(NUM_PAD[i], NUM_PAD[j], is_num_pad=True):
            cost = 0
            for x, y in itertools.pairwise('A'+p):
                cost += lookup.get((x, y), 1)
            if cost < shortest:
                shortest = cost
        cost_map[(i, j)] = shortest 
    return cost_map            
    
def get_complexity(code, num_robots):
    cost_map = calculate_cost_map(num_robots)
    sum = 0
    for i, j in itertools.pairwise('A' + code):
        sum += cost_map[(i, j)] * int(code[:-1])
    return sum
    
@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    codes = []
    for line in file.readlines():
        codes.append(line.strip())
    print(part1(codes))
    print(part2(codes))



if __name__ == "__main__":
    main(sys.argv[1:])
