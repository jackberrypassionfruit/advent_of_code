
from util import Node, QueueFrontier
from termcolor import colored
import sys, time

class HillClimbing():
  def _find_start_and_end(self):
    for row_index, row in enumerate(self.heightmap):
      for col_index, val in enumerate(row):
        match val:
          case 'S':
            self.start = (col_index, row_index)
          case 'E':
            self.end = (col_index, row_index)         
  
  def __init__(self):
    self.heightmap = []
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
      for line in infile:
        self.heightmap.append(line.rstrip('\n'))
    self.height = len(self.heightmap)
    self.width = len(self.heightmap[0])
    self._find_start_and_end() # start is 🌈, end is 🏁
    
    self.frontier = QueueFrontier()
    self.traveled_path = []

  def __repr__(self):    
    result = self.heightmap
    for row_index, row in enumerate(result):
      result[row_index] = row.replace('S', "\N{rainbow}").replace('E', '\N{chequered flag}')
    return '\n'.join(result)

  # def print_frontier(self):
  #   print('Current frontier:')
  #   for node in self.frontier.frontier: # the QueueFrontier class has its own frontiere attribute....sigh
  #     print(node)
      
  # def print_traveled_path(self):
  #   print('Traveled path')
  #   # for coord in self.traveled_path:
  #   #   print(str(coord))
  #   print(self.traveled_path)
      
  def get_next_move_options(self, state, x, y):
    
    next_steps = []
    
    # if (x, y) == self.start:
    #   this_ord = 100
    # else:
    #   this_ord = ord(self.heightmap[y][x])
    
    this_ord = 100 if (x, y) == self.start else ord(self.heightmap[y][x])
    
    # self.heightmap[y][x-1] = self.heightmap[y][x-1]
    # self.heightmap[y][x+1] = self.heightmap[y][x+1]
    # self.heightmap[y+1][x] = self.heightmap[y+1][x]
    # self.heightmap[y-1][x] = self.heightmap[y-1][x]
    
    
    if x > 0               and (state == 'z' or self.heightmap[y][x-1] != 'E') and ord(self.heightmap[y][x-1]) <= this_ord + 1:
      next_steps.append((self.heightmap[y][x-1], x-1, y))
    if x < self.width - 1  and (state == 'z' or self.heightmap[y][x+1] != 'E') and ord(self.heightmap[y][x+1]) <= this_ord + 1:
      next_steps.append((self.heightmap[y][x+1], x+1, y))
    if y > 0               and (state == 'z' or self.heightmap[y-1][x] != 'E') and ord(self.heightmap[y-1][x]) <= this_ord + 1:
      next_steps.append((self.heightmap[y-1][x], x, y-1))
    if y < self.height - 1 and (state == 'z' or self.heightmap[y+1][x] != 'E') and ord(self.heightmap[y+1][x]) <= this_ord + 1:
      next_steps.append((self.heightmap[y+1][x], x, y+1))
      
    real_next_steps = []
    for state, x, y in next_steps:
      if (x, y) not in self.traveled_path and (x, y) not in self.frontier.get_frontier_coords(): ####### or frontier!!:
        real_next_steps.append((state, x, y))
    
    return real_next_steps
    
    
    
  def compile_path(self, node):
    num_steps = 0
    path = []
    while node.parent:
      num_steps += 1
      path.append({
        'state': node.state,
        'coord': node.coord,
        'action': node.action
      })
      node = node.parent
      
    for step in reversed(path):
      print(step)
    for row_index, row in enumerate(self.heightmap):
      for col_index, val in enumerate(row):
        for step in path:
          if (col_index, row_index) == step['coord']:
            val = colored(step['action'], 'green')
            break
        print(val, end='')
      print()

    
    return num_steps
  
  def find_shortest_path(self):
    self.frontier.add(Node(state='S', coord=self.start, parent=None, action=None))
    
    while self.frontier:
      # self.print_frontier()
      current_node = self.frontier.remove()            
      self.traveled_path.append(current_node.coord)
      # print(f'current -> state: {current_node.state}, coord: {current_node.coord}')
      # print('next moves: ', self.get_next_move_options(current_node.state, *current_node.coord))
      # self.print_traveled_path()
      # print('Traveled path: ', self.traveled_path)
      if current_node.state == 'E':
        return print(self.compile_path(current_node))
      else:
        # for state, x, y in self.get_next_move_options(*current_node.coord):
        for state, x, y in self.get_next_move_options(current_node.state, *current_node.coord):
          if (x, y) not in self.traveled_path:
            if   x > current_node.coord[0]:
              action = '>'
            elif x < current_node.coord[0]:
              action = '<'
            elif y > current_node.coord[1]:
              action = 'V'
            elif y < current_node.coord[1]:
              action = '^'
            self.frontier.add(Node(
              state = state,
              coord = (x, y),
              parent = current_node,
              action = action
            ))
            # print(f'adding {state} ({x}, {y}) to frontier')
        # self.print_frontier()
        # print(self.frontier)
        # print('\n')
        # print(self.compile_path(current_node))
        # print('\n\n\n\n')
        # time.sleep(.5)
            