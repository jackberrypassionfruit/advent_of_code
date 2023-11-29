

class RopePhysics():
  def __init__(self, actions):
    self.tail_x = 0
    self.tail_y = 0
    self.head_x = 0
    self.head_y = 0
    
    self.tails_travels = set()
    
    self.actions = actions
    x, y, max_x, max_y = 0, 0, 0, 0
    for action in actions:
      dir, dist = action
      if dir == 'R':
        x += dist
        max_x = max(x, max_x)
      elif dir == 'L':
        x -= dist
      elif dir == 'U':
        y += dist
        max_y = max(y, max_y)
      elif dir == 'D':
        y -= dist
    
    self.max_x = max_x
    self.max_y = max_y
      
  def __repr__(self):
    return f'head_x: {self.head_x}, head_y: {self.head_y}'
    
  def move_head_one_space(self, dir):
    if   dir == 'R':
      self.head_x += 1
    elif dir == 'L':
      self.head_x -= 1
    elif dir == 'U':
      self.head_y += 1
    elif dir == 'D':
      self.head_y += 1
    # TODO
    # Add functionality to make the tail trail behind the head
      
  def draw_board(self):
    head_y = self.max_y - self.head_y - 1
    tail_y = self.max_y - self.tail_y - 1
    board = ''
    for y in range(self.max_y):
      for x in range(self.max_x):
        if   x == self.head_x and y == head_y:
          board += 'H'
        elif x == self.tail_x and y == tail_y:
          board += 'T'
        else:
          board += '.'
      board += '\n'
    print(board)