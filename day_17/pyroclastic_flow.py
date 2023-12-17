import sys

class FallingRocks():
  def __init__(self):
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
      jet_push_text = infile.read()
    self.jet_gas = ''.join(jet_push_text.split('\n'))
    
    self.blocks = [
      ['####'],
      [
        '.#.',
        '###',
        '.#.'
      ],
      # this next one is flipped because I'm storing the playfield upside down in memory
      [
        '###',
        '..#',
        '..#'
      ],
      [ 
        '#',
        '#',
        '#',
        '#'
      ],
      [
        '##',
        '##'
      ]
    ]
      
    self.feeld = '''\
..####.
.......
.......
.......
.......\
'''.split('\n')

    self.current_loc = [2,1]
    
  def __repr__(self):
    block_index = 4
    result = ''
    for line_index, line in enumerate(self.feeld):
      block_row = line_index - self.current_loc[1]
      if  0 <= block_row < len(self.blocks[block_index]):
        block_line = ''
        for col in range(7):
          block_col = col - self.current_loc[0]
          if self.current_loc[0] <= col <= len(self.blocks[block_index][block_row]) + 1:
            block_line += self.blocks[block_index][block_row][block_col]
          else:
            block_line += '.'
        result += f'{block_line}\n'
      else:
        result += f'{line}\n'
          
          
          
    # return result
    return '\n'.join(reversed(result.split('\n'))) # Flip the image upside down
  
  def check_if_will_collide(self):
    raise NotImplementedError
    
  