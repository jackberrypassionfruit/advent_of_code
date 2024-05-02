

with open('input.txt', 'r') as infile:
  bits = infile.read().split('\n')
  
bits = [int(bit) for bit in bits]

print('\n'.join( [str(bit) for bit in sorted(bits)] ))
