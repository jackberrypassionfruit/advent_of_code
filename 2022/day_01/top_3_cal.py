first = None
second = None
third = None

elf_end = False

with open ('input.txt', 'r') as infile:
  lines = infile.readlines()
  
# print(input)

sum = 0
cals = []

for cal in lines:
  if cal == '\n':
  #   print('yes')
    cals.append(sum)
    sum = 0
  else:
    sum += int(cal)
    
cals.sort(reverse=True)
print(cals)
print(cals[0] + cals[1] + cals[2])