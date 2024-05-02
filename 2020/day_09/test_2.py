
import bisect 
import sys

PREVIOUS_INVALID = 675280050
# PREVIOUS_INVALID = 127

with open('input.txt', 'r') as infile:
  xmax_strings = infile.read().split('\n')
xmax_strings = [int(num) for num in xmax_strings]

# premable = sorted(xmax_strings[:PREAMBLE_LENGTH])
  
# def is_contiguous_sum(premable):
i, j = 0, 1

while j < len(xmax_strings):
  this_series = xmax_strings[i:j+1]
  this_sum = sum(this_series)
  # print(f'this_series: {this_series}')
  if this_sum == PREVIOUS_INVALID:
    # for num in sorted(this_series):
    sorted_series = sorted(this_series)
    print(f'{sorted_series[0]} + {sorted_series[-1]} = {sorted_series[0] + sorted_series[-1]}')

    sys.exit()
  elif this_sum < PREVIOUS_INVALID:
    j += 1
  elif this_sum > PREVIOUS_INVALID:
    i += 1
print('could not find')
  

# for i in range(PREAMBLE_LENGTH, len(xmax_strings)):
#   # print(f'premable: {premable} <> ', end='')
#   next_preamble_num = xmax_strings[i]
#   if is_valid_preamble_num(premable, next_preamble_num):
#     # print('Issa match!')
#     pass
#   else:
#     print(f'failed next_preamble_num: {next_preamble_num}')
#     # print('fuck')
#   premable.remove(xmax_strings[i - PREAMBLE_LENGTH])
#   bisect.insort(premable, next_preamble_num)

