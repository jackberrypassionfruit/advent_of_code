from functools import reduce

def my_ord(num: str) -> int:
  num = ord(num)
  num %= 96
  if num > 64:
    return num % 64 + 26
  else:
    return num

with open('input.txt', 'r') as infile:
  lines = infile.readlines()

sum = 0
group = []
count = 0

for line in lines:
  rucksack = line.strip()
  # print(rucksack)
  group.append(set(rucksack))
  count += 1
  
  if count == 3:
    count = 0
    # print(group)
    intersects = group[0] & group[1] & group[2]
    # print(intersects)
    for char in intersects:
      sum += my_ord(char)
    group = []
    
print(sum)