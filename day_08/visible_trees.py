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

# vis_trees = (width * 4) - 4
max_scenic_score = 0
for i in range(1, width - 1):
  for j in range(1, width - 1):
    num = rows[j][i]
    left = rows[j][:i]
    left_view = 1
    for tree_height_index, tree_height in enumerate(left[::-1]):
      if tree_height >= num:
        break
      elif tree_height_index < len(left) - 1:
        left_view += 1
    right = rows[j][i+1:]
    right_view = 1
    for tree_height_index, tree_height in enumerate(right[:-1]):
      if tree_height >= num:
        break
      elif tree_height_index < len(right) - 1:
        right_view += 1
    above = cols[i][:j]
    above_view = 1
    for tree_height_index, tree_height in enumerate(above[::-1]):
      if tree_height >= num:
        break
      elif tree_height_index < len(above) - 1:
        above_view += 1
    below = cols[i][j+1:]
    below_view = 1
    for tree_height_index, tree_height in enumerate(below[:-1]):
      if tree_height >= num:
        break
      elif tree_height_index < len(below) - 1:
        below_view += 1
    scenic_score = left_view * right_view * above_view * below_view
    max_scenic_score = max(max_scenic_score, scenic_score)
    if max_scenic_score == scenic_score:
      
      print(f'scenic_score: {scenic_score},\ni: {i},\nj: {j},\nnum: {num},\nleft: {left},\nright: {right},\nabove: {above},\nbelow: {below}\n,left_view: {left_view}\n,right_view: {right_view}\n,above_view: {above_view}\n,below_view: {below_view}\n\n')
    
    
    
#     if num > max(left) or num > max(right) or num > max(above) or num > max(below):
#       vis_trees += 1
      
# print(vis_trees)
print(max_scenic_score)