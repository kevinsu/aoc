import sys
from collections import defaultdict
from common.perf import profiler

def toggle(instruction):
  if len(instruction) == 2:
    cmd = 'dec' if instruction[0] == 'inc' else 'inc'
    return [cmd, instruction[1]]
  cmd = 'cpy' if instruction[0] == 'jnz' else 'jnz'
  return [cmd, instruction[1], instruction[2]]

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

def update_registers_with_snapshot(registers, snapshot):
  inc_target = None
  dec_target = None
  for key, value in snapshot.items():
    if value == registers[key]:
      continue 
    if registers[key] - value > 0:
      inc_target = key
    if registers[key] - value < 0:
      dec_target = key
  dec_value = registers[dec_target]
  dec_diff = registers[dec_target] - snapshot[dec_target]
  inc_diff = snapshot[inc_target] - registers[inc_target]
  multiplier = int(dec_value / dec_diff) 
  registers[dec_target] -= multiplier * dec_diff 
  registers[inc_target] += multiplier * inc_diff
  
def get_int_or_register(registers, value):
  try:
    return int(value)
  except:
    return registers.get(value, 0)

def execute(instructions, init, limit):
  registers = {'a' : init}
  i = 0
  last_20 = []
  snapshot = {}
  alternator = -1
  count = 0
  while i >= 0 and i < len(instructions):
    instruction = instructions[i]
    last_20 = (last_20+[instruction])[-20:]
    if instruction[0] == 'out':
      
      transmit = get_int_or_register(registers, instruction[1])
      if transmit == alternator:
        return False
      count += 1
      alternator = transmit
      if count > limit:
        return True
      i+=1
      continue
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
      if last_20[-6:-3] == last_20[-3:]:
        update_registers_with_cycle(registers, last_20[-3:])
      if instruction[2] == '-5':
        if snapshot:
          update_registers_with_snapshot(registers, snapshot)
          snapshot = {}
        else: 
          snapshot = registers.copy()
      if get_int_or_register(registers, instruction[1]) == 0:
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
  i = 0 
  success = False
  while not success:
    i+=1
    print(f"Trying a={i}")
    success = execute(instructions, i, 1000)
  print(f"Succeeded with a={i}")
  

if __name__ == "__main__":
  main(sys.argv[1:])
