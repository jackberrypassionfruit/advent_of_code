score = 0

with open ('input.txt', 'r') as infile:
  lines = infile.readlines()
  
for round in lines:
  hands = round.strip().split(' ')
  opp = hands[0]
  me = hands[1]
  
  if me == 'X':
    score += 1
    if opp == 'C':
      score += 6
    elif opp == 'A':
      score += 3
  elif me == 'Y':
    score += 2
    if opp == 'A':
      score += 6
    elif opp == 'B':
      score += 3
  elif me == 'Z':
    score += 3
    if opp == 'B':
      score += 6
    elif opp == 'C':
      score += 3

print(score)