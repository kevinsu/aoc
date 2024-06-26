import hashlib
import sys
from common.perf import profiler
from dataclasses import dataclass


@dataclass
class Directions:
    up: bool
    down: bool
    left: bool
    right: bool

    def __init__(self):
        return

    def __str__(self):
        return f"up: {self.up}, down: {self.down}, left: {self.left}, right: {self.right}"


@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    passcode = file.readline()
    path = bfs(passcode)
    print(path)
    print(len(path))

def bfs(passcode):
    q = [(0, 0, '')]
    while q:
        current = q.pop(0)
        x = current[0]
        y = current[1]
        path = current[2]
        if x == 3 and y == 3:
            return current[2]
        directions = get_directions(passcode, path)
        if directions.up and y > 0:
            q.append((x, y-1, path+'U'))
        if directions.down and y < 3:
            q.append((x, y+1, path+'D'))
        if directions.left and x > 0:
            q.append((x-1, y, path+'L'))
        if directions.right and x < 3:
            q.append((x+1, y, path+'R'))
        
        
def get_directions(passcode, path):
    result = hashlib.md5((passcode+path).encode()).hexdigest()
    directions = Directions()
    directions.up = is_open(result[0])
    directions.down = is_open(result[1])
    directions.left = is_open(result[2])
    directions.right = is_open(result[3])
    return directions


def is_open(c):
    return c in ['b', 'c', 'd', 'e', 'f']


if __name__ == "__main__":
    main(sys.argv[1:])
