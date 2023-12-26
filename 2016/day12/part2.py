import sys
from collections import defaultdict
from common.perf import profiler

def toggle(instruction):
  if len(instruction) == 2:
    cmd = 'dec' if instruction[0] == 'inc' else 'inc'
    return [cmd, instruction[1]]
  cmd = 'cpy' if instruction[0] == 'jnz' else 'jnz'
  return [cmd, instruction[1], instruction[2]]

def get_int_or_register(registers, value):
  try:
    return int(value)
  except:
    return registers.get(value, 0)

def update_registers_with_cycle(registers, instructions):
  increments = defaultdict(int)
  target = None
  for instruction in instructions:
    if instruction[0] == 'inc':
      increments[instruction[1]] += 1 
    elif instruction[0] == 'dec':
      increments[instruction[1]] -= 1
    elif instruction[0] == 'jnz':
      target = instruction[1]
    else:
      raise Exception ("not implemented")
  multiplier = registers[target] / increments[target]
  for key, value in increments.items():
    registers[key] -= int(value * multiplier)
  


def execute(instructions):
  registers = {'c' : 1}
  i = 0
  last_six = []
  while i >= 0 and i < len(instructions):
    instruction = instructions[i]
    last_six = (last_six + [instruction])[-6:]
    if instruction[0] == 'cpy':
      if len(instruction) < 3:
        print('invalid: %s, length' % instruction)
        i+=1
        continue
      if instruction[2].isdigit():
        print('invalid: %s, register is digit' % instruction)
        i+=1
        continue
      registers[instruction[2]] = get_int_or_register(registers, instruction[1]) 
    if instruction[0] == 'tgl':
      if len(instruction) == 3:
        print('invalid: %s, toggle 2 instructions' % instruction)
      jump = get_int_or_register(registers, instruction[1])
      new_i = i + jump 
      if new_i < 0 or new_i >= len(instructions):
        i+=1
        continue
      instructions[new_i] = toggle(instructions[new_i])
    if instruction[0] == 'inc':
      if instruction[1].isdigit():
        print('invalid: %s, not a register' % instruction)
        i+=1
        continue
      registers[instruction[1]] = registers.get(instruction[1], 0) + 1 
    if instruction[0] == 'dec':
      if instruction[1].isdigit():
        print('invalid: %s, not a register' % instruction)
        i+=1
        continue
      registers[instruction[1]] = registers.get(instruction[1], 0) - 1 
    if instruction[0] == 'jnz':
      if last_six[0:3] == last_six[3:6]:
        update_registers_with_cycle(registers, last_six[0:3])        
        last_six = []
      if get_int_or_register(registers, instruction[1]) == 0:
        print('skipped: %s, jnz on 0' % instruction)
        i+=1
        continue
      i += get_int_or_register(registers, instruction[2]) 
      continue
    i+=1
  print(registers['a'])

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  instructions = []
  for line in file.readlines():
    instructions.append(line.split())
  execute(instructions)

if __name__ == "__main__":
  main(sys.argv[1:])
