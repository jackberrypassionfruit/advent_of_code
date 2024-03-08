import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

def get_cube_np_arrays(x = 0, y = 0, z = 0):   
    phi = np.arange(1,10,2)*np.pi/4
    Phi, Theta = np.meshgrid(phi, phi)
    
    x = np.array([[val + x + 0.5 for val in array] for array in np.cos(Phi)*np.sin(Theta) ])
    y = np.array([[val + y + 0.5 for val in array] for array in np.sin(Phi)*np.sin(Theta) ])
    z = np.array([[val + z + 0.5 for val in array] for array in np.cos(Theta)/np.sqrt(2) ])
    
    return x,y,z

def render_cubes_from_coords(coords):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  max_x = max(map(lambda coord: coord[0], coords))
  min_x = min(map(lambda coord: coord[0], coords))
  max_y = max(map(lambda coord: coord[1], coords))
  min_y = min(map(lambda coord: coord[1], coords))
  max_z = max(map(lambda coord: coord[2], coords))
  min_z = min(map(lambda coord: coord[2], coords))
  ax.set_xlim(min_x-1, max_x+2)
  ax.set_ylim(min_y-1, max_y+2)
  ax.set_zlim(min_z-1, max_z+2)
  

  for coord in coords:
    x,y,z = get_cube_np_arrays(*coord)
    ax.plot_surface(x, y, z)

  plt.show()

with open(sys.argv[1], 'r', encoding='utf8') as infile:
  file_text = infile.readlines()
  
coords = []
for line in file_text:
  coords.append([int(num) for num in line.split(',')])


render_cubes_from_coords(coords)

