from rope_bridge import *
import sys, json

with open (sys.argv[1], 'r') as infile:
  lines = infile.readlines()
  
actions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
# for action in actions:
#   print(action)

# rope_physics_short = RopePhysicsShort(actions)
# # rope_physics_short._calculate_board_size(actions)
# # rope_physics_short.draw_board()
# rope_physics_short.perform_actions()



# # rope_physics_short.draw_board(show_path=True)
# print(rope_physics_short.get_tail_path_count())


rope_physics_long = RopePhysicsLong(actions)
rope_physics_long.perform_actions()
rope_physics_long.draw_board(show_path=True)
print(rope_physics_long.get_tail_path_count())
# print(rope_physics_long._calculate_board_size(actions))


# test = range(5, 0, -1)
# for i in test:
#   print(i)


### answer is SMALLER THAN 2561