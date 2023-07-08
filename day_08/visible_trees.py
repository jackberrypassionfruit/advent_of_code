import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
### The problem with this code is that I am not correctly getting the next line
# or something like that
# what I need to do is reset the logic so the loop is actually on the "next" line
# and interior line uses that cache to check each value
# will involve some rewriting
count = 0
previous_line = lines[0].rstrip('\n')
current_line = lines[1].rstrip('\n')
# next_line = lines[2].rstrip('\n')
for int_line_index, interior_line in enumerate(lines[2:]):
  # next_line = interior_line.rstrip('\n')
  print(interior_line[1:-2])
  for i in range(1, 4): # checking each char in $interior_line
    print('digit_index: ', i)
    print('previous_line', previous_line)
    print('next_line', next_line)
    print('digits to check')
    print('top', previous_line[i])
    print('bot', next_line[i])
    print('lef', interior_line[i - 1])
    print('rit', interior_line[i + 1])
    print('END digits to check')
    if int(previous_line[i]) >= int(interior_line[i]):
      # print(interior_line[i], end=' ')
      count += 1
    elif int(next_line[i]) >= int(interior_line[i]):
      # print(interior_line[i], end=' ')
      count += 1
    elif int(interior_line[i - 1]) >= int(interior_line[i]):
      # print(interior_line[i], end=' ')
      count += 1
    elif int(interior_line[i + 1]) >= int(interior_line[i]):
      # print(interior_line[i], end=' ')
      count += 1
    
    print('')
  previous_line = current_line
  current_line = next_line
  next_line = lines[int_line_index].rstrip('\n')
    
  
    
  