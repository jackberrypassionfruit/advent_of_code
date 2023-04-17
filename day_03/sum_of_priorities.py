sum = 0

def my_ord(num: str) -> int:
  num = ord(num)
  num %= 96
  if num > 64:
    return num % 64 + 26
  else:
    return num

with open ('input.txt', 'r') as infile:
  lines = infile.readlines()
  
for line in lines:
  rucksack = line.strip()
  cuttoff = int(len(rucksack) /2)
  first = rucksack[:cuttoff]
  second = rucksack[cuttoff:]
  intersects = set(first) & set(second)

  for char in intersects:
    sum += my_ord(char)
print(sum)

# print(my_ord('p'))
# print(my_ord('L'))