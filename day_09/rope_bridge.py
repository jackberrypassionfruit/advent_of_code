

class RopePhysics():
  
  def _calculate_board_size(self, actions):
    x, y, max_x, max_y = 0, 0, 0, 0
    for action in actions:
      dir, dist = action
      if   dir == 'R':
        x += dist
        max_x = max(x, max_x)
      elif dir == 'L':
        x -= dist
      elif dir == 'U':
        y += dist
        max_y = max(y, max_y)
      elif dir == 'D':
        y -= dist
      # print(f'x: {x}, y: {y}, max_x: {max_x}, max_y: {max_y}')
    return max_x+1, max_y+1
  
  def __init__(self, actions):
    self.tail_x = 0
    self.tail_y = 0
    self.head_x = 0
    self.head_y = 0
    
    self.tails_travels = set()
    
    self.actions = actions
    self.max_x, self.max_y = self._calculate_board_size(actions)
      
  def __repr__(self):
    return f'head_x: {self.head_x}, head_y: {self.head_y}'
  
  def draw_board(self, show_path=False):
    head_y = self.max_y - self.head_y - 1
    tail_y = self.max_y - self.tail_y - 1
    board = ''
    for y in range(self.max_y):
      for x in range(self.max_x):
        if show_path and (x, y) in self.tails_travels:
          board += '#'
        elif not show_path and x == self.head_x and y == head_y:
          board += 'H'
        elif not show_path and x == self.tail_x and y == tail_y:
          board += 'T'
        else:
          board += '.'
      board += '\n'
    print(board)
    # if show_path:
    #   print(self.tails_travels)
    
  def _tail_follow_head(self):
    x_diff = self.head_x - self.tail_x
    y_diff = self.head_y - self.tail_y
    if   abs(x_diff) > 1:
      self.tail_x += (x_diff / 2)
      self.tail_y = self.head_y
    elif abs(y_diff) > 1:
      self.tail_y += (y_diff / 2)
      self.tail_x = self.head_x
    
  def move_head_one_space(self, dir):
    if   dir == 'R':
      self.head_x += 1
    elif dir == 'L':
      self.head_x -= 1
    elif dir == 'U':
      self.head_y += 1
    elif dir == 'D':
      self.head_y -= 1
      
    self._tail_follow_head()
    self.tails_travels.update([(self.tail_x, self.max_y-self.tail_y-1)])
    # self.draw_board()
    
  def perform_actions(self):
    for action in self.actions:
      dir, dist = action
      for i in range(dist):
        self.move_head_one_space(dir)
        
  def get_tail_path_count(self):
    return len(self.tails_travels)