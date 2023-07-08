import sys

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
def first_unique_nums(datastream: str) -> str:
  char_index = 14
  buffer = datastream[:14]
  new_char = datastream[char_index]
  # print("buffer:", buffer, ", new_char", new_char)
  while len(list(buffer)) != len(set(list(buffer))):
    buffer = buffer[1:] + new_char
    char_index += 1
    new_char = datastream[char_index]
    # print("buffer:", buffer, ", new_char", new_char)
    
  return char_index
  
  
line_num = 1
for line in lines:
  print(line_num, "-", first_unique_nums(line), "\n")

# first_unique_four(lines[0])