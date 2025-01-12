import sys
from common.perf import profiler

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  
  def __str__(self):
    return f'({self.value}, {self.next.value}, {self.prev.value})'

def get_node_with_value(head, i):
  while head.value != i:
    head = head.next
  return head

def get_nth(head, num, offset):
  offset = offset % num
  while offset > 0:
    head = head.next
    offset -= 1
  return head.value

def build_zero_index_list(zero_head):
  l = []
  node = get_node_with_value(zero_head, 0)
  while True:
    l.append(node.value)
    node = node.next
    if node == zero_head:
      break
  return l

def part1(head, num, zero_node, initial_position_map):
  node = head  
  for i in range(num):    
    node = initial_position_map[i]
    node_prev = node.prev
    node_next = node.next
    target = node
    if node.value == 0:      
      continue
    value = node.value % (num-1)    
    while value > 0:
      target = target.next
      value -= 1
    node.prev = target
    node.next = target.next
    target.next.prev = node
    target.next = node
    node_prev.next = node_next
    node_next.prev = node_prev              
  l = build_zero_index_list(zero_node)
  return l[1000] + l[2000] + l[3000]
  
KEY = 811589153
def part2(head, num, zero_node, initial_position_map):
  node = head  
  for _ in range(10):
    for i in range(num):    
      node = initial_position_map[i]
      node_prev = node.prev
      node_next = node.next
      target = node
      if node.value == 0:      
        continue
      value = (node.value * KEY) % (num-1)    
      while value > 0:
        target = target.next
        value -= 1
      node.prev = target
      node.next = target.next
      target.next.prev = node
      target.next = node
      node_prev.next = node_next
      node_next.prev = node_prev              
  l = build_zero_index_list(zero_node)
  return KEY*(l[1000] + l[2000] + l[3000])
  
def read_input(lines):
  head = None
  prev = None
  index = 0
  node = None
  zero_node = None
  initial_position_map = {}
  for line in lines:
    node = Node(int(line))
    if node.value == 0:
      zero_node = node
    initial_position_map[index] = node
    if not head:
      head = node
    if prev:
      prev.next = node
      node.prev = prev      
    prev = node
    index += 1    
  node.next = head
  head.prev = node
  return head, index, zero_node, initial_position_map

@profiler
def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  lines = []
  for line in file.readlines():
    lines.append(line)
  head, index, zero_node, initial_position_map = read_input(lines)
  print(part1(head, index, zero_node, initial_position_map))
  
  head, index, zero_node, initial_position_map = read_input(lines)  
  print(part2(head, index, zero_node, initial_position_map))

if __name__ == "__main__":
  main(sys.argv[1:])

