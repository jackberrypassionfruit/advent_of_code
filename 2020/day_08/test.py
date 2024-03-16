import json, time

with open('input.txt', 'r') as infile:
  instructions_str = infile.read().split('\n')

instructions_list = [line.split(' ') for line in instructions_str]
instructions_dict = [dict({'word': line[0], 'num': int(line[1])}) for line in instructions_list]


# print(json.dumps(instructions_dict, indent=4))

path = set()
acc = 0
i = 0

# print(f'i: {i}, acc: {acc}')  
while i not in path:
  path.update({i})
  word = instructions_dict[i]['word']
  num = instructions_dict[i]['num']
  if word == 'acc':
    acc += num
  elif word == 'jmp':
    i += num - 1
  i += 1
  # print(f'i: {i}, acc: {acc}, word: {word}')  
  # time.sleep(0.05)
# print(f'\nacc: {acc}')

# for i, i_instruct in enumerate(instructions_str):
#   if i in path:
#     print(f'{i_instruct} - {i}')
#   else:
#     print(i_instruct)


for i in range(len(instructions_dict) - 1, -1, -1):
  word = instructions_dict[i]['word']
  num = instructions_dict[i]['num']
  
  if i in path and word == 'jmp' and num < 0:
    print(f'i: {i}')
    instructions_dict[i-1]['word'] = 'nop'
    break
    
    
    
    
# do it again!
path = set()
acc = 0
i = 0

# print(f'i: {i}, acc: {acc}')  
while True:
  path.update({i})
  word = instructions_dict[i]['word']
  num = instructions_dict[i]['num']
  # print(f'i: {i}, acc: {acc}, word: {word}, num: {num}')
  if word == 'acc':
    acc += num
  elif word == 'jmp':
    i += num - 1
  i += 1
  if i == len(instructions_dict):
    print('you did it!')
    break
  time.sleep(0.001)
print(f'\nacc: {acc}')

''' 1140 is too low '''

