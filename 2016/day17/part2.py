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


max_length = 0


@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    passcode = file.readline()
    dfs(passcode, 0, 0, '')
    print(max_length)


def dfs(passcode, x, y, path):
    if x == 3 and y == 3:        
        global max_length    
        max_length = max(len(path), max_length)
        return
    directions = get_directions(passcode, path)
    if directions.up and y > 0:
        dfs(passcode, x, y-1, path+'U')
    if directions.down and y < 3:
        dfs(passcode, x, y+1, path+'D')
    if directions.left and x > 0:
        dfs(passcode, x-1, y, path+'L')
    if directions.right and x < 3:
        dfs(passcode, x+1, y, path+'R')


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
