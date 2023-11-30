from rope_bridge import RopePhysics
import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
actions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
# for action in actions:
#   print(action)

rope_physics = RopePhysics(actions)
# rope_physics._calculate_board_size(actions)
# rope_physics.draw_board()
rope_physics.perform_actions()



# rope_physics.draw_board(show_path=True)
print(rope_physics.get_tail_path_count())