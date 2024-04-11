
import bisect 

PREAMBLE_LENGTH = 25

with open('input.txt', 'r') as infile:
  xmax_strings = infile.read().split('\n')
xmax_strings = [int(num) for num in xmax_strings]

premable = sorted(xmax_strings[:PREAMBLE_LENGTH])

# for num in xmax_strings:
#   print(num)
  
def is_valid_preamble_num(premable, next_preamble_num):
  i, j = 0, PREAMBLE_LENGTH - 1
  
  while j - i > 0:
    current_sum = premable[i] + premable[j]
    if current_sum == next_preamble_num:
      # print(f'{premable[i]} + {premable[j]} = {next_preamble_num} ', end='')
      return True
    elif current_sum < next_preamble_num:
      i += 1
    elif current_sum > next_preamble_num:
      j -= 1
  return False
  


for i in range(PREAMBLE_LENGTH, len(xmax_strings)):
  # print(f'premable: {premable} <> ', end='')
  next_preamble_num = xmax_strings[i]
  if is_valid_preamble_num(premable, next_preamble_num):
    # print('Issa match!')
    pass
  else:
    print(f'failed next_preamble_num: {next_preamble_num}')
    # print('fuck')
  premable.remove(xmax_strings[i - PREAMBLE_LENGTH])
  bisect.insort(premable, next_preamble_num)
    
  
# this_bool = is_valid_preamble_num(premable, xmax_strings[0])
# print(f'this_bool: {this_bool}')

