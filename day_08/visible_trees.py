import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
width = len(lines[0].rstrip('\n'))
# print(width)
rows = [list(row.rstrip('\n')) for row in lines]
# print(rows)

cols = []
for col in range(width):
  cols.append([row[col] for row in lines])
# print(cols)

for i in range(width):
  for j in range(width):
    pass
    # TODO
    # check if the given tree is the max of the trees above, below, left, and right of it