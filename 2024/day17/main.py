from math import floor
import re
import sys
from common.perf import profiler


class Debugger:

    def __init__(self, a, b, c, instructions):
        self.a = a
        self.b = b
        self.c = c
        self.instructions = instructions
        self.instruction_pointer = 0
        self.output = []
    
    def __str__(self):
        return f'{self.a} {self.b} {self.c} {self.instruction_pointer} {",".join(list(map(str, self.instructions)))}'

    def get_combo(self, operand):
        combo = operand
        if operand == 4:
            combo = self.a
        elif operand == 5:
            combo = self.b
        elif operand == 6:
            combo = self.c
        elif operand >= 7:
            raise Exception("Invalid operand: ", operand)
        return combo

    def adv(self, operand):
        self.a = floor(self.a / (2 ** self.get_combo(operand)))
        self.instruction_pointer += 2

    def bxl(self, operand):
        self.b = self.b ^ operand
        self.instruction_pointer += 2

    def bst(self, operand):
        combo = self.get_combo(operand)
        self.b = combo % 8
        self.instruction_pointer += 2

    def jnz(self, operand):
        if self.a == 0:
            self.instruction_pointer += 2
            return
        self.instruction_pointer = operand

    def bxc(self, _):
        self.b = self.b ^ self.c
        self.instruction_pointer += 2

    def out(self, operand):
        combo = self.get_combo(operand)
        self.output.append(combo%8)
        self.instruction_pointer += 2

    def bdv(self, operand):
        self.b = floor(self.a / (2 ** self.get_combo(operand)))
        self.instruction_pointer += 2

    def cdv(self, operand):
        self.c = floor(self.a / (2 ** self.get_combo(operand)))
        self.instruction_pointer += 2

    def switch(self, opcode, operand):        
        map = {0: self.adv,
               1: self.bxl,
               2: self.bst,
               3: self.jnz,
               4: self.bxc,
               5: self.out,
               6: self.bdv,
               7: self.cdv
               }
        map[opcode](operand)

    def run(self):
        if self.instruction_pointer >= len(self.instructions):
            return self.output
        opcode = self.instructions[self.instruction_pointer]
        operand = self.instructions[self.instruction_pointer+1]
        self.switch(opcode, operand)
        self.run()


def part1(a, b, c, instructions):
    debugger = Debugger(a, b, c, instructions)
    debugger.run()
    return debugger.output    

def test1():
    debugger = Debugger(0, 0, 9, [2, 6])
    debugger.run()
    assert debugger.b == 1

def test2():
    debugger = Debugger(10, 0, 0, [5, 0, 5, 1, 5, 4])
    debugger.run()
    print(debugger.output)
    assert debugger.output == []  

goal = []
def part2(a, b, c, instructions):
    # Find the first two patterns that match
    # Fine the next pattern that matches
    num_matched = 0
    for i in range(0, 120000):
        output = part1(i, b, c, instructions)        
        if output[0:num_matched] == instructions[0:num_matched]:
          print(i, num_matched, output )
          if len(output) > num_matched and output[num_matched] == instructions[num_matched]:
              num_matched += 1
          
        
def solve(a, depth, instructions):
    if (depth == len(instructions)):
        return a
    for i in range(0, 8):
        next_a = (a << 3) + i
        debugger = Debugger(next_a, 0, 0, instructions)
        debugger.run()
        output = debugger.output        
        if output == instructions[len(instructions)-1-depth:]:
            result = solve(next_a, depth + 1, instructions)
            if result != None:
                return result
    return None

@profiler
def main(argv):
    input_file = argv[0]
    file = open(input_file, 'r')
    match = re.match(
        r'Register\s\w:\s(\d+)\nRegister\s\w:\s(\d+)\nRegister\s\w:\s(\d+)\s*Program:\s(.*)$', file.read())
    a, b, c, instructions = int(match.group(1)), int(match.group(2)), int(
        match.group(3)), list(map(int, match.group(4).strip().split(",")))
    #part1(a, b, c, instructions)
    #print(part1(1129486, 0, 0, [2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0] ))
    #part2(a, b, c, instructions)
    print(solve(0, 0, instructions))
    #test2()


if __name__ == "__main__":
    main(sys.argv[1:])
