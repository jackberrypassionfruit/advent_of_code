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

vis_trees = (width * 4) - 4
for i in range(1, width - 1):
  for j in range(1, width - 1):
    left = rows[j][:i]
    right = rows[j][i+1:]
    above = cols[i][:j]
    below = cols[i][j+1:]
    num = rows[j][i]
    if num > max(left) or num > max(right) or num > max(above) or num > max(below):
      # print(f'i: {i},\nj: {j},\nnum: {num},\nleft: {left},\nright: {right},\nabove: {above},\nbelow: {below}\n\n')
      vis_trees += 1
      
print(vis_trees)