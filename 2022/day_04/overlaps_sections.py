import sys

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
def check_if_assignment_overlaps(assignment_pairs: list) -> bool:
  first = assignment_pairs[0].split('-')
  second = assignment_pairs[1].split('-')
  
  if int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]):
    return True
  elif int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1]):
    return True
  elif int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1]):
    return True
  elif int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1]):
    return True
  else:
    return False
  
  
count = 0
line_num = 1
for line in lines:
  assignment_pairs = line.strip().split(',')
  if check_if_assignment_overlaps(assignment_pairs):
    print(str(line_num), assignment_pairs)
    count += 1
  line_num += 1
  
print(count)