from rope_bridge import RopePhysics

import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
actions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
# for action in actions:
#   print(action)

rope_physics = RopePhysics(actions)
rope_physics.move_head_one_space('U')
rope_physics.move_head_one_space('R')
# # print(rope_physics)

rope_physics.draw_board()