score = 0

with open ('input.txt', 'r') as infile:
  lines = infile.readlines()
  
for round in lines:
  hands = round.strip().split(' ')
  opp = hands[0]
  outcome = hands[1]
    
  if outcome == 'X':
    # score += 0
    if opp == 'A':
      score += 3
    elif opp == 'B':
      score += 1
    elif opp == 'C':
      score += 2
  elif outcome == 'Y':
    score += 3
    if opp == 'A':
      score += 1
    elif opp == 'B':
      score += 2
    elif opp == 'C':
      score += 3
  elif outcome == 'Z':
    score += 6
    if opp == 'A':
      score += 2
    elif opp == 'B':
      score += 3
    elif opp == 'C':
      score += 1

print(score)