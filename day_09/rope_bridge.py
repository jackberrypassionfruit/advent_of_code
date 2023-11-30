class RopePhysicsShort():
  
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
  
  def draw_board(self, show_path=False):
    head_y = self.max_y - self.head_y - 1
    tail_y = self.max_y - self.tail_y - 1
    board = ''
    for y in range(self.max_y):
      for x in range(self.max_x):
        if show_path and [x, y] in self.tails_travels:
          board += '#'
        elif not show_path and x == self.head_x and y == head_y:
          board += 'H'
        elif not show_path and x == self.tail_x and y == tail_y:
          board += 'T'
        else:
          board += '.'
      board += '\n'
    print(board)
    
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
  
class RopePhysicsLong():
  
  def _calculate_board_size(self, actions):
    x, y, max_x, max_y, min_x, min_y = 0, 0, 0, 0, 0, 0
    for action in actions:
      dir, dist = action
      if   dir == 'R':
        x += dist
        max_x = max(x, max_x)
      elif dir == 'L':
        x -= dist
        min_x = min(x, min_x)
      elif dir == 'U':
        y += dist
        max_y = max(y, max_y)
      elif dir == 'D':
        y -= dist
        min_y = min(y, min_y)
    return max_x+1, max_y+1, min_x, min_y
  
  def __init__(self, actions):    
    self.knots = [[0, 0] for i in range(10)]
    self.tails_travels = set()
    
    self.actions = actions
    self.max_x, self.max_y, self.min_x, self.min_y = self._calculate_board_size(actions)
  
  def draw_board(self, show_path=False):
    mirror_knots = [[knot[0], self.max_y + self.min_y - knot[1] - 1] for knot in self.knots]
    board = ''
    for y in range(self.min_y, self.max_y):
      for x in range(self.min_x, self.max_x):
        if show_path and tuple([x, y]) in self.tails_travels:
          board += '#'
        elif  not show_path and [x, y] == mirror_knots[9]:
          board += 'H'
        elif not show_path and [x, y] in mirror_knots:
          for knot_index in range(len(mirror_knots) - 2 , -1, -1): # range(8 -> 0)
            if [x, y] == mirror_knots[knot_index]:
              board += str(knot_index + 1)
              break
        else:
          board += '.'
      board += '\n'
    print(board)
    
  def move_head(self, dir):
    match dir:
      case 'R':
        self.knots[9][0] += 1
      case 'L':
        self.knots[9][0] -= 1
      case 'U':
        self.knots[9][1] += 1
      case 'D':
        self.knots[9][1] -= 1
    
  def all_knots_follow(self):
    for knot_index in range(len(self.knots) - 2 , -1, -1): # range(8 -> 0)
      lo_knot = self.knots[knot_index]
      hi_knot = self.knots[knot_index + 1]
      
      x_diff = hi_knot[0] - lo_knot[0]
      y_diff = hi_knot[1] - lo_knot[1]
      
      if   abs(x_diff) > 1:
        lo_knot[0] += int(x_diff / 2)
        if abs(y_diff) > 1:
          lo_knot[1] += int(y_diff / 2)
        else:
          lo_knot[1] = hi_knot[1]
      elif abs(y_diff) > 1:
        lo_knot[1] += int(y_diff / 2)
        if abs(x_diff) > 1:
          lo_knot[0] += int(x_diff / 2)
        else:
          lo_knot[0] = hi_knot[0]
        
      self.knots[knot_index] = lo_knot
      self.knots[knot_index + 1] = hi_knot
        
  def make_step(self, dir):
    self.move_head(dir)
    self.all_knots_follow()
    self.tails_travels.update([(self.knots[0][0], self.max_y + self.min_y-self.knots[0][1]-1)])
    # self.draw_board()
    # print(self.knots)
    
    
  def perform_actions(self):
    for action in self.actions:
      dir, dist = action
      for i in range(dist):
        self.make_step(dir)
        
  def get_tail_path_count(self):
    return len(self.tails_travels)