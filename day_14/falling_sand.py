import sys, time

class SandyCave():  
  def __init__(self):
    with open(sys.argv[1], 'r') as infile:
      cave_wall_paths = infile.readlines()
      
    self.resting_sand = set()
    self.wall_paths = set()
    self.x_min, self.x_max, self.y_max = 1000, 0, 0
    
    for path in cave_wall_paths:
      i = 0
      path = path.rstrip('\n').split(' -> ')
      path = [point.split(',') for point in path]
      while i < len(path) - 1:
        x_0, y_0, x_1, y_1 = int(path[i][0]), int(path[i][1]), int(path[i+1][0]), int(path[i+1][1])
        self.y_max = max(self.y_max, y_0, y_1)
        self.x_min = min(self.x_min, x_0, x_1)
        self.x_max = max(self.x_max, x_0, x_1)
        if   y_0 < y_1:
          for y in range(y_0, y_1 + 1):
            self.wall_paths.update([(x_0, y)])
        elif y_0 > y_1:
          for y in range(y_1, y_0 + 1):
            self.wall_paths.update([(x_0, y)])
        elif x_0 < x_1:
          for x in range(x_0, x_1 + 1):
            self.wall_paths.update([(x, y_0)])
        elif x_0 > x_1:
          for x in range(x_1, x_0 + 1):
            self.wall_paths.update([(x, y_0)])
        i += 1
        
  def __repr__(self):
    result = ''
    for j in range(self.y_max + 1 + 2):
      for i in range(self.x_min, self.x_max + 1):
        if   (i, j) == (500, 0):
          result += '+'
        elif j == self.y_max + 2:
          result += 'F'
        elif (i, j) in self.resting_sand | {self.current_coords}:
          result += 'O'
        elif (i, j) in self.wall_paths:
          result += '#'
        else:
          result += '.'
      result += '\n'
    return result
      
  def next_possible_moves(self, x, y):
    return [(x, y) for x, y in [(x, y+1), (x-1, y+1), (x+1, y+1)] if  
              (x, y) not in self.wall_paths and \
              (x, y) not in self.resting_sand and \
              (x, y) != self.current_coords and \
              y < self.y_max + 2]
  def drop_sand(self):
    self.current_coords = (500, 0)
    can_move = True
    while can_move:
      possible_moves = self.next_possible_moves(*self.current_coords)
      if not possible_moves and self.current_coords == (500, 0):
        self.current_coords = None
        return False 
      elif not possible_moves:
        self.resting_sand.add(self.current_coords)
        can_move = False
      # elif possible_moves[0][0] < self.x_min or possible_moves[0][0] > self.x_max or possible_moves[0][1] > self.y_max:
        # self.current_coords = None
        # return False
      else:
        self.current_coords = possible_moves[0]
      # print(self)
    print(f'Current count: {len(self.resting_sand)}')
    # time.sleep(.1)
    return True
      
  def cave_collapse(self):
    cont = True
    while cont:
      cont = self.drop_sand()
    

    print(self)
    print(f'Final count: {len(self.resting_sand)}')
      