import sys
from common.perf import profiler

def concatenate(a, b):
    return int(str(a) + str(b))

def can_equal(goal, so_far, values):
    if len(values) == 0:
        return goal == so_far
    if so_far == 0:
        return can_equal(goal, 1 * values[0], values[1:]) or can_equal(goal, 0 + values[0], values[1:])
    else:
        return can_equal(goal, so_far * values[0], values[1:]) or can_equal(goal, so_far + values[0], values[1:])


def part1(input):
    sum = 0
    for goal, values in input.items():
      if can_equal(goal, 0, values):
          sum += goal
    return sum

def can_equal2(goal, so_far, values):
    #print(so_far, values)
    if so_far > goal:
       return False
    if len(values) == 0:
        return goal == so_far
    add = can_equal2(goal, so_far + values[0], values[1:])
    mul = None
    if so_far == 0:
      mul = can_equal2(goal, values[0], values[1:])
    else:
      mul = can_equal2(goal, so_far * values[0], values[1:])
    con = False
    if len(values) >= 1:
      con = can_equal2(goal, concatenate(so_far, values[0]), values[1:])
    return add or mul or con


def part2(input):
    sum = 0
    for goal, values in input.items():
      print(goal, values)
      if can_equal2(goal, 0, values):          
          sum += goal
      else:
         
         print('fail: ', goal, values)
    return sum

@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    input = {}
    for line in file.readlines():
        colon_split = line.split(':')
        input[int(colon_split[0])] = list(map(int, colon_split[1].split()))
    #print(part1(input))
    print(part2(input))
    #print(can_equal2(7290,0, [6, 8, 6, 15]))
    #print(can_equal2(156 ,0, [15, 6]))
    #print(can_equal2(192 ,0, [17, 8, 14]))


if __name__ == "__main__":
    main(sys.argv[1:])
