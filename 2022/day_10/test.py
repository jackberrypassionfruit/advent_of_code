import sys

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
actions = [[line[:4], line[5:].rstrip('\n'), 2 if line[:4] == 'addx' else 1] for line in lines]
# print(actions)
# for action in actions:
#   print(action)

register = 1
cycle_num = 1
signal_strength_sum = 0
ptr = 0

while cycle_num <= 220:
  
  instruction, v, clock = actions[ptr]
  
  if (cycle_num - 20) % 40 == 0:
    signal_strength = register * cycle_num
    signal_strength_sum += signal_strength
    # print(f'cycle_num: {cycle_num}, instruction: {instruction}, register: {register}, v: {v}, signal_strength: {signal_strength}, ptr: {ptr}')
    print(f'cycle_num: {cycle_num}, register: {register}, v: {v}, signal_strength: {signal_strength}, ptr: {ptr}')
    
  
  if instruction == 'addx':
    if clock == 2:
      actions[ptr][2] -= 1
    elif clock == 1:
      register += int(v)
      ptr += 1
  else:
    ptr += 1
      
  cycle_num += 1


print(signal_strength_sum)