from monkey_business import *

from math import lcm

# print(lcm(11, 7 , 13, 5 , 3 , 17, 2 , 19))

keep_away = MonkeyBusinessSlow()

for i in range(10000):
  print(f'round: {i}')
  # print(keep_away)
  keep_away.monkey_round()
print(keep_away.calculate_monkey_business())

# keep_away = MonkeyBusinessFast()


# for i in range(10000):
#   print(f'round: {i}')
#   # print(keep_away)
#   keep_away.item_round()

# keep_away.print_current_items()
# # keep_away.print_current_monkey_inspects()