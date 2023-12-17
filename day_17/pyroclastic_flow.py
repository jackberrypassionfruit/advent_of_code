import sys, math

class FallingRocks():
  def __init__(self):
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
      jet_push_text = infile.read()
    self.jet_gas = ''.join(jet_push_text.split('\n'))
    
    self.blocks = [
      ['@@@@'],
      [
        '.@.',
        '@@@',
        '.@.'
      ],
      # this next one is flipped because I'm storing the playfield upside down in memory
      [
        '@@@',
        '..@',
        '..@'
      ],
      [ 
        '@',
        '@',
        '@',
        '@'
      ],
      [
        '@@',
        '@@'
      ]
    ]
      
    # testing
    self.block_carcasses = set({ (2,0), (3,0), (4,0), (5,0) })
    self.feeld = '''\
..####.
.......
.......
.......
.......\
'''.split('\n')

    self.current_loc = [2,1]
    self.block_index = 2

    
  def __repr__(self):
    result = ''
    for line_index, line in enumerate(self.feeld):
      block_row = line_index - self.current_loc[1]
      # if self.current_loc == [0,0], then yet to drop a new block
      if self.current_loc != [0,0] and 0 <= block_row < len(self.blocks[self.block_index]):
        block_line = ''
        for col in range(7):
          block_col = col - self.current_loc[0]
          if self.current_loc[0] <= col <= len(self.blocks[self.block_index][block_row]) + 1:
            block_line += self.blocks[self.block_index][block_row][block_col]
          else:
            block_line += '.'
        result += f'{block_line}\n'
      else:
        result += f'{line}\n'
          
          
          
    # return result
    return '\n'.join(reversed(result.split('\n'))) # (Un)Flip the image upside down
  
  def get_current_block_coords(self):  
    block_coords = set()
    for block_row_index, block_row in enumerate(self.blocks[self.block_index]):
      for block_col_index, block_col in enumerate(block_row):
        if block_col != '.':
          new_block_spot_x, new_block_spot_y = self.current_loc
          new_block_spot_x += block_col_index
          new_block_spot_y += block_row_index
          block_coords.update([(new_block_spot_x, new_block_spot_y)])
    return block_coords
    
  def check_if_will_collide(self):
    potential_collisions = set()
    current_block_coords = self.get_current_block_coords()
    for block_spot in current_block_coords:
      collision_spot_x, collision_spot_y = block_spot
      collision_spot_x -= 1
      collision_spot_y -= 1
      potential_collisions.update([(collision_spot_x, collision_spot_y)])
    return potential_collisions.intersection(self.block_carcasses)
  
  def stop_block(self):
    block_coords = self.get_current_block_coords()
    for coords in block_coords:
      coord_x, coord_y = coords
      self.feeld[coord_y] = self.feeld[coord_y][:coord_x] + '#' + self.feeld[coord_y][coord_x+1:]
    self.current_loc = [0,0]
    #TODO add a return value, max_height, which will be max(current_max_height, max_height_of_this_dead_block)
    