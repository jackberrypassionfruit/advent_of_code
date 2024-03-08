

with open('test_input.txt', 'r') as infile:
  password_list = infile.read().split('\n')
  
print(f'password_list: {password_list}')