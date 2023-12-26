import sys
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

def execute(instructions):
  registers = {'c' : 1}
  i = 0
  while i >= 0 and i < len(instructions):
    instruction = instructions[i]
    print("NEXT: \n\n")
    print(i, instruction)
    print(registers)
    print("\n".join(map(str, instructions)))
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
      if get_int_or_register(registers, instruction[1]) == 0:
        print('invalid: %s, jnz on 0' % instruction)
        i+=1
        continue
      i += get_int_or_register(registers, instruction[2]) 
      continue
    i+=1

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
