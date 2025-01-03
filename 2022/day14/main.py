import sys
from common.perf import profiler
from itertools import pairwise
from common.io import pretty_print


class Cave:
    def __init__(self, min_x, max_x, max_y, lines):
        self.source_x = 500
        self.source_y = 0
        self.min_x = min_x
        self.max_x = max_x
        self.max_y = max_y
        self.grid = [['.']*(max_x-min_x+1) for i in range(max_y+1)]
        self.count = 0
        self.set(self.source_x, self.source_y, '+')    
        for line in lines:
            self.add_line(line)
    
    def set(self, x, y, c):
        self.grid[y][x-self.min_x] = c   

    def get(self, x, y):
        return self.grid[y][x-self.min_x] 

    def add_line(self, line):
        x1, y1, x2, y2 = line    
        dx = x2-x1
        if dx != 0:
            dx = int(dx/abs(dx))
        dy = y2-y1
        if dy != 0:
            dy = int(dy/abs(dy))
        cx = x1
        cy = y1
        while cx != x2 or cy !=y2:
            self.set(cx, cy, '#')
            cx = cx + dx
            cy = cy + dy
        self.set(cx, cy, '#')

    def in_grid(self, x, y):
        return x >= self.min_x and x <= self.max_x and y < self.max_y
    
    def get_next_open(self):
        cx = self.source_x
        cy = self.source_y
        while self.in_grid(cx, cy):
            # Check down
            if self.get(cx, cy+1) == '.':
                cy = cy+1
                continue
            elif self.get(cx-1, cy+1) == '.':
                cx = cx-1
                cy = cy+1
                continue
            elif self.get(cx+1, cy+1) == '.':
                cx = cx+1
                cy = cy+1            
            else:
                if (cx, cy) == (self.source_x, self.source_y): 
                  self.count += 1                 
                  return None
                return cx, cy
        return None        

    def add_sand(self):
        opening = self.get_next_open()
        while opening is not None:
            x, y = opening
            self.set(x, y, 'o')
            self.count += 1
            opening = self.get_next_open()        
        
def part1(min_x, max_x, max_y, lines):
    cave = Cave(min_x, max_x, max_y, lines)
    cave.add_sand()
    return cave.count

def part2(min_x, max_x, max_y, lines):
    cave = Cave(min_x-max_y, max_x+max_y, max_y+2, lines)
    cave.add_line((min_x-max_y, max_y+2, max_x+max_y, max_y+2))
    cave.add_sand()  
    return cave.count  

@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    lines = set()
    min_x = 500
    max_x = 500
    max_y = 0
    for line in file.readlines():
        points = line.split("->")
        for p1, p2 in pairwise(points):
            x1, y1 = map(int, p1.strip().split(","))
            x2, y2 = map(int, p2.strip().split(","))
            min_x = min(min(x1, min_x), x2)
            max_x = max(max(x1, max_x), x2)
            max_y = max(max(y1, max_y), y2)
            lines.add((x1, y1, x2, y2))
    print(part1(min_x, max_x, max_y, lines))
    print(part2(min_x, max_x, max_y, lines))


if __name__ == "__main__":
    main(sys.argv[1:])
