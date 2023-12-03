import sys

class HillClimbing():
  def __init__(self):
    self.heightmap = []
    with open(sys.argv[1], 'r', encoding='utf-8') as infile:
      for line in infile:
        self.heightmap.append(line.rstrip('\n'))

  def __repr__(self):
    return '\n'.join(self.heightmap)
  
  def get_next_move_options(self, x, y):
  # TODO
    pass