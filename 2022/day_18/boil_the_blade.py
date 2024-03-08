import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

class BoilingBoulders():
  def __init__(self):
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
      self.coords = [[int(num) for num in line.split(',')] for line in infile.readlines()]
      
  def get_cube_np_arrays(self, x = 0, y = 0, z = 0):   
    phi = np.arange(1,10,2)*np.pi/4
    Phi, Theta = np.meshgrid(phi, phi)
    
    x = np.array([[val + x + 0.5 for val in array] for array in np.cos(Phi)*np.sin(Theta) ])
    y = np.array([[val + y + 0.5 for val in array] for array in np.sin(Phi)*np.sin(Theta) ])
    z = np.array([[val + z + 0.5 for val in array] for array in np.cos(Theta)/np.sqrt(2) ])
    
    return x,y,z
  
  def render_cubes_from_coords(self):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    max_x = max(map(lambda coord: coord[0], self.coords))
    min_x = min(map(lambda coord: coord[0], self.coords))
    max_y = max(map(lambda coord: coord[1], self.coords))
    min_y = min(map(lambda coord: coord[1], self.coords))
    max_z = max(map(lambda coord: coord[2], self.coords))
    min_z = min(map(lambda coord: coord[2], self.coords))
    ax.set_xlim(min_x-1, max_x+2)
    ax.set_ylim(min_y-1, max_y+2)
    ax.set_zlim(min_z-1, max_z+2)
    
    for coord in self.coords:
      x,y,z = self.get_cube_np_arrays(*coord)
      ax.plot_surface(x, y, z)

    plt.show()
    
  def get_neighbor_coords(self, coord):
    neighbor_coords = []
    for i in range(-1, 2):
      for j in range(-1, 2):
        for k in range(-1, 2):
          if (i,j,k) != (0,0,0) and ((i,j) == (0,0) or (j,k) == (0,0) or (k,i) == (0,0)):
            neighbor_coords.append([coord[0] + i, coord[1] + j, coord[2] + k])
    print('coord: ', coord)
    print('neighboor_coords: ', neighbor_coords)    
    return neighbor_coords
  def count_surface_area(self):
    self.surface_area = 0
    for coord in self.coords:
      neighbor_coords = self.get_neighbor_coords(coord)
      for neighbor_coord in neighbor_coords:
        if neighbor_coord not in self.coords:
          self.surface_area += 1
      print('surface_area: ', self.surface_area)
    return self.surface_area