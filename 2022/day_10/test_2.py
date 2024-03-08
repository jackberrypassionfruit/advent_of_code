import sys

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
actions = [[line[:4], line[5:].rstrip('\n'), 2 if line[:4] == 'addx' else 1] for line in lines]
# print(actions)
# for action in actions:
#   print(action)

length_input = len(actions)
register = 1
col = 0
ptr = 0

while ptr < length_input:
  
  instruction, v, clock = actions[ptr]
  
  
  if col % 40 == 0 and col != 0:
    print('')
    col = 0
  
  if abs(col - register) <= 1:
    print('#', end='')
  else:
    print('.', end='')
    
  
  if instruction == 'addx':
    if clock == 2:
      actions[ptr][2] -= 1
    elif clock == 1:
      register += int(v)
      ptr += 1
  else:
    ptr += 1
      
  col += 1
