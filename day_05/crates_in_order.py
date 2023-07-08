import sys

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
columns = [
  list(reversed([ "V", "R", "H", "B", "G", "D", "W" ])),
  list(reversed([ "F", "R", "C", "G", "N", "J" ])),
  list(reversed([ "J", "N", "D", "H", "F", "S", "L" ])),
  list(reversed([ "V", "S", "D", "J" ])),
  list(reversed([ "V", "N", "W", "Q", "R", "D", "H", "S" ])),
  list(reversed([ "M", "C", "H", "G", "P" ])),
  list(reversed([ "C", "H", "Z", "L", "G", "B", "J", "F" ])),
  list(reversed([ "R", "J", "S" ])),
  list(reversed([ "M", "V", "N", "B", "R", "S", "G", "L" ]))
]

  
line_num = 1
for line in lines[10:]:
  num_crates = int(line[5:7])
  col_from = int(line[12:14]) - 1
  col_to = int(line[17:19]) - 1
  print(str(line_num), "-", num_crates, col_from, col_to)
  
  crate_buffer = []
  for i in range(num_crates):
    crate_moving = columns[col_from].pop()
    # print("crate_moving: ", crate_moving)
    crate_buffer.append(crate_moving)
    
  crate_buffer.reverse()
  
  for buff_index, buff in enumerate(crate_buffer):
    columns[col_to].append(buff)
  
  # print("next col!\n")
  line_num += 1
for col_index, col in enumerate(columns):
  print(col_index+1, "-", col[-1])
  
for col_index, col in enumerate(columns):
  print(col[-1], end='')